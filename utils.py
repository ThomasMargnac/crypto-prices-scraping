def cleaning_price(
    price: str
):
    # Removing $ sign
    price = price.replace("$", "")
    # From str to float
    price = float(price)
    return price