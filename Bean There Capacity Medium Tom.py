#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:33:06 2024

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

# Filter the data for 'Medium roast'
filtered_data = Roasting[Roasting['Product type'] == 'Medium roast']

# Pivot the data to organize it for plotting
pivot_data = filtered_data.groupby('Month')['Weight p/hour'].sum()

# Create the figure and the first subplot
plt.figure(figsize=(10, 12))  # Increase height for two plots

# First subplot
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(pivot_data.index, pivot_data.values, marker='o', color='b')

# Add horizontal lines
plt.axhline(y=215, color='black', linestyle='--', linewidth=2)
plt.axhline(y=182.75, color='orangered', linestyle='--', linewidth=2)

# Set y-axis limits
plt.ylim(80, 220)  # Start y-axis from 140

# Add labels and title
plt.title('Weight per Hour per Month for Medium Roast')
plt.xlabel('Month')
plt.ylabel('Weight p/hour')
plt.xticks(rotation=45)  # Rotate the x-axis labels if necessary

# Adjust layout and show the plots
plt.tight_layout()
plt.show()








