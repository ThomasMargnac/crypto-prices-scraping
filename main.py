from crypto import Price

if __name__ == "__main__":
	bitcoin = Price("bitcoin")
	price = bitcoin.get()
	print(price)