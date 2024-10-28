#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:06:56 2024

@author: Tom
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet 'Roasting' from the Excel file
file_path = 'Bean there done that data.xlsx'
Roasting = pd.read_excel(file_path, sheet_name='Roasting')

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Ensure 'Month' is treated as a categorical type
Roasting['Month'] = pd.Categorical(Roasting['Month'], categories=month_order, ordered=True)
Roasting['Month'] = Roasting['Month'].apply(lambda x: x[:3])

# Create the 'Weight p/hour' column
Roasting['Weight p/hour'] = (Roasting['Number of batches per day'] * 
                             Roasting['Load weight p/batch']) / 8

# Filter the data for 'Dark Roast' and 'Light Roast'
filtered_data = Roasting[Roasting['Product type'].isin(['Dark Roast', 'Light Roast'])]

# Pivot the data to organize it for plotting
pivot_data = filtered_data.groupby('Month')['Weight p/hour'].sum()

# Create the figure and the first subplot
plt.figure(figsize=(10, 12))  # Increase height for two plots

# First subplot
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(pivot_data.index, pivot_data.values, linewidth=5, color='orangered')

# Add horizontal lines
plt.axhline(y=480, color='grey', linestyle='-', linewidth=2)
plt.axhline(y=408, color='black', linestyle='--', linewidth=2)

# Set y-axis limits
plt.ylim(0, 500)

# Dynamically set x-axis limits based on where the data begins and ends
plt.xlim(pivot_data.index.min(), pivot_data.index.max())

# Add the title using text, aligned slightly to the left
plt.gca().text(-0.046, 1.05, 'Underutilization', color='orangered', fontsize=16, weight='bold', transform=plt.gca().transAxes)  # Align title to the left

# Add text to the right of the title
plt.text(0.22, 1.05, 'Probat Px120 (in kg/h)', color='black', weight='bold', fontsize=16, ha='left', transform=plt.gca().transAxes)

# Add labels for the horizontal lines on the right y-axis
plt.text(len(pivot_data.index) - 0.9, 480, 'Capacity', color='grey', va='center', ha='left', fontsize=11, weight='bold')
plt.text(len(pivot_data.index) - 0.9, 408, 'Occupancy rate', color='black', va='center', ha='left', fontsize=11, weight='bold')

# Add label for the Weight p/hour line
plt.text(len(pivot_data.index) - 0.9, pivot_data.values[-1], 'Avg weight', color='orangered', va='center', ha='left', fontsize=11, weight='bold')

# Remove top and right spines (axes)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Remove x-axis and y-axis labels
plt.gca().set_xlabel('')
plt.gca().set_ylabel('')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

#KPI = Ensure that the deviation in roasting consumption does not exceed 10% of the occupancy rate.
#Advice is to roast more beans and therefor increase the sales, instead of making costs due to underutilization. Or to invest in a (probably) less expensive machines whose occupancy rate meets the consumption and therefor doesn't cost costs of underutilization
