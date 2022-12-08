def cleaning_price(
	price: str
):
	# Removing $ sign
	price = price.replace("$", "")
	# Removing , sign
	price = price.replace(",", "")
	# From str to float
	price = float(price)
	# Returning price
	return price