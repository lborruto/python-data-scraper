import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

def draw2 ():
	
	# Introducing variables
	x = []
	y1 = []
	y2 = []

	# Collecting the csv data of the BitCoin's value evolution
	with open('2016-01-01_2021-11-09_bitcoinprice_org.csv', 'r') as csvfile:
		btc = csv.reader(csvfile, delimiter = ';')

		for row in btc:
			x.append(date.fromisoformat(row[0]))
			y1.append(int(row[1]))

	# Collecting the csv data of the Ethereum's value evolution
	with open('2016-01-01_2021-11-09_ethereumprice_org.csv', 'r') as csvfile:
		eth = csv.reader(csvfile, delimiter = ';')

		for row in eth:
			y2.append(int(row[7]))

	# Create a figure containing the two axes.
	fig, ax_b = plt.subplots()
	ax_b.plot(x, y1, color='tab:blue')
	ax_e = ax_b.twinx()
	ax_e.plot(x, y2, color='tab:orange')

	# Add the labels of the 'y' column in the same color as the axes
	ax_b.set_ylabel('BitCoin', color='tab:blue')
	ax_e.set_ylabel('Ethereum', color='tab:orange')

	# Printing the figure
	plt.show()