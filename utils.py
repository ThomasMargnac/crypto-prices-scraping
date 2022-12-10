import re

def cleaning_price(
	price: str
):
	# Removing all characters except for digits and point
	price = re.sub(r'[^0-9.]', '', price)
	# From str to float
	price = float(price)
	# Returning price
	return price