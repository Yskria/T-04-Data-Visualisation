#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:30:52 2024

@author: Tom
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

# Load the specific sheet 'E-com sales orders by product' from the Excel file
file_path = '/Users/Tom/Downloads/Bean there done that data.xlsx'
ecom_sales = pd.read_excel(file_path, sheet_name='E-com sales orders by product')

# Filter the data where the value is greater than or equal to 55
ecom_sales_above = ecom_sales[ecom_sales['Value'] >= 55]

# Filter for Delivery Fee of 0 and 4.95
filtered_data = ecom_sales_above[ecom_sales_above['Delivery fee'].isin([0, 4.95])]

# Create a DataFrame for the counts of each delivery fee
fee_counts = filtered_data['Delivery fee'].value_counts().sort_index()

# Prepare data for stacked bar chart
labels = ['Orders']
values_495 = fee_counts.get(4.95, 0)  # Aantal orders met een delivery fee van €4.95
values_0 = fee_counts.get(0, 0)  # Aantal orders met een delivery fee van €0

# Create a horizontal stacked bar chart
plt.figure(figsize=(6, 2))  # Increase the height for better visibility

# Plot the €4.95 bar
plt.barh(labels, values_495, color='orangered', label='€4.95')

# Stack the €0 bar on top of the €4.95 bar
plt.barh(labels, values_0, left=values_495, color='lightgrey', label='€0')

# Add titles and labels
plt.title('Orders Wrongly Charged with', loc='left', weight='bold', fontsize=14, color='black')  # Align title to the left
plt.xlabel('Amount of Orders > €55')

# Add text to the right of the title
plt.text(0.585, 1.08, 'Delivery Fees', color='orangered', weight='bold', fontsize=14, ha='left', transform=plt.gca().transAxes)

# Remove the top and right spines (axes)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Remove the y-axis spine and ticks
plt.gca().spines['left'].set_visible(False)  # Verberg de y-as spine
plt.gca().set_yticks([])  # Verberg de y-as ticks


# Format the x-axis with 'k' for thousands, rounded up to the nearest thousand
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{math.ceil(x / 1000)}k' if x >= 1000 else str(math.ceil(x))))

# Add x-axis label for total orders with €0 delivery fee, rounded up
plt.text(values_495, -0.59, f'{math.ceil(values_495 / 1000)}k' if values_495 >= 1000 else f'{math.ceil(values_495)}', color='orangered', fontsize=10, va='center', ha='center')

# Add a tick mark at the position of values_495
plt.xticks(list(plt.xticks()[0]) + [values_495], color='black')  # Voeg een tick mark toe op values_495

# Set the x-axis limits to fit the bars
plt.xlim(0, values_495 + values_0 + 10)  # Voeg wat extra ruimte toe voor duidelijkheid

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
