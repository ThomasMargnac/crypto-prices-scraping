from crypto import Price

if __name__ == "__main__":
	bitcoin = Price("bitcoin")
	price1, lower1, higher1 = bitcoin.get()
	price2, lower2, higher2 = bitcoin.get()
	print(bitcoin.dataframe)