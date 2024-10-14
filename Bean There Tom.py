#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:30:52 2024

@author: Tom
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet 'E-com sales orders by product' from the Excel file
file_path = '/Users/Tom/Downloads/Bean there done that data.xlsx'
ecom_sales = pd.read_excel(file_path, sheet_name='E-com sales orders by product')

# Filter the data where the value is greater than or equal to 55
ecom_sales_above = ecom_sales[ecom_sales['Value'] >= 55]

# Filter for Delivery Fee of 0 and 4.95
filtered_data = ecom_sales_above[ecom_sales_above['Delivery fee'].isin([0, 4.95])]

# Create a bar chart showing the count of each 'Delivery fee'
plt.figure(figsize=(10, 6))
fee_counts = filtered_data['Delivery fee'].value_counts().sort_index()

# Create bars with different colors
colors = ['lightgrey' if fee == 0 else 'red' for fee in fee_counts.index]
bar_width = 0.4  # Width of the bars

# Plot bars closely together by adjusting the position
plt.bar(fee_counts.index, fee_counts.values, color=colors, width=bar_width)

# Add titles and labels
plt.title('Total of orders above €55 with delivery fee\'s')
plt.xlabel('Delivery Fee')
plt.ylabel('Number of Orders')

# Set x-ticks to show only 0 and 4.95
plt.xticks([0, 4.95], ['0', '4.95'])

# Remove the top and right spines (axes)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Format the y-axis with thousands separators
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Show the plot
plt.tight_layout()  # Adjust layout to fit labels
plt.show()



#kijken naar hoe veel er wordt ingekocht per product (purchased) (ten opzichte van elkaar)?
#kijken naar het verbruik aan producten (zie stock level)?
#kijkend naar verlies (Damaged + expired) (mss ook kijkend naar de leverancier)
#mss is er een correlatie tussen leverancier en product?
#data geeft alleen maanden weer en niet jaartal (2023)
#stock value is 4 (bij het eerste product), 4,25 bij 2de product
#kijkend naar de waardes per product (zie voorgaande regel)

#misschien een overzicht/planning van stock op basis van inkoop en verbruik
#misschien een eigen gemaakte capacity voor de warehouse hebben, of zo min mogelijk in de warehouse (wel rekening houdend met seizoen en buffer etc)
#vergelijk de 2 verschillende roasters (welke werkt efficienter/effectiever)
#er gaat iets fout met aankopingen boven 55 zonder transportkosten (E-commerce)
#misschien locatie van vestiging wijzigen op basis van locatie van de meeste leveringen
