import requests
from bs4 import BeautifulSoup
from utils import cleaning_price

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
        # Requesting page
        response = requests.get(url)
        # Preparing my soup
        soup = BeautifulSoup(response.content, features="html.parser")
        # Getting price
        price = soup.find('div', attrs={'class': 'priceValue'})
        price = cleaning_price(price)
        # Returning data
        return price