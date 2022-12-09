def cleaning_price(
	price: str
):
	# Removing "$" sign
	price = price.replace("$", "")
	# Removing "," sign
	price = price.replace(",", "")
	# Removing "Low:"
	price = price.replace("Low:", "")
	# Removing "High:"
	price = price.replace("High:", "")
	# From str to float
	price = float(price)
	# Returning price
	return price