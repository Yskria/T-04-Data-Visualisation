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

# Create the 'Weight p/hour' column
Roasting['Weight p/hour'] = (Roasting['Number of batches per day'] * 
                             Roasting['Load weight p/batch']) / 8

# Filter the data for 'Dark Roast' and 'Light Roast'
filtered_data_dark_light = Roasting[Roasting['Product type'].isin(['Dark Roast', 'Light Roast'])]

# Pivot the data to organize it for plotting
pivot_data_dark_light = filtered_data_dark_light.groupby('Month')['Weight p/hour'].sum()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(pivot_data_dark_light.index, pivot_data_dark_light.values, marker='o', color='b')

# Add horizontal lines
plt.axhline(y=480, color='black', linestyle='--', linewidth=2)  # Black dashed line at 480
plt.axhline(y=408, color='orangered', linestyle='--', linewidth=2)  # Orangered dashed line at 408

# Add labels and title
plt.title('Weight per Hour per Month for Dark and Light Roast')
plt.xlabel('Month')
plt.ylabel('Weight p/hour')
plt.xticks(rotation=45)  # Rotate the x-axis labels if necessary

# Adjust layout and show the plot
plt.tight_layout()
plt.show()


