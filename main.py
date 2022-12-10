from crypto import Price

if __name__ == "__main__":
	bitcoin = Price("bitcoin")
	time1, price1, lower1, higher1, circulatingSupply1 = bitcoin.get()
	time2, price2, lower2, higher2, circulatingSupply2 = bitcoin.get()
	print(bitcoin.dataframe)