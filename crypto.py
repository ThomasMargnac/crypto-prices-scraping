import requests
from bs4 import BeautifulSoup
from utils import cleaning_price
import pandas as pd
from datetime import datetime

class Price():
	def __init__(
		self,
		currency: str
	):
		"""
		Initialize Price object

		Parameters
		----------
		currency: str
			Crypto-currency you want to track
		"""
		# Verifying parameter's type
		if not isinstance(currency, str):
			raise TypeError("currency must be str, yours is {}".format(type(currency)))
		# Defining currency
		self.currency = currency
		# Defining Dataframe to save history
		self.dataframe = pd.DataFrame(columns = ['Time', 'Price', 'Lower', 'Higher'])

	def get(
		self
	):
		"""
		Getting current currency price

		Returns
		-------
		float
			Price of current currency
		"""
		# Path to currency page
		url = "https://coinmarketcap.com/currencies/{}/".format(self.currency)
		# Getting time
		time = datetime.utcnow()
		# Requesting page
		response = requests.get(url)
		# Preparing my soup
		soup = BeautifulSoup(response.content, features="html.parser")
		# Getting price
		priceSection = soup.find('div', attrs={'class': 'priceSection'})
		price = priceSection.find('div', attrs={'class': 'priceValue'})
		price = cleaning_price(price.text)
		# Getting lower and higher price in the last 24h
		volatilitySection = soup.find('div', attrs={'class': 'sliderSection'})
		# Removing unwanted div
		slider = volatilitySection.find('div', attrs={'class': 'slider'})
		slider.extract()
		namePillBase = volatilitySection.find('div', attrs={'class': 'namePillBase'})
		namePillBase.extract()
		volatilityPrices = volatilitySection.findChildren('div')
		lower = cleaning_price(volatilityPrices[0].text)
		higher = cleaning_price(volatilityPrices[1].text)
		# Saving to history dataframe
		data = pd.DataFrame(
			{
				'Time': [time],
				'Price': [price],
				'Lower': [lower],
				'Higher': [higher]
			}
		)
		self.dataframe = pd.concat(
			[self.dataframe, data],
			ignore_index=True
		)
		# Returning data
		return price, lower, higher