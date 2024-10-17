#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:42:34 2024

@author: Tom
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet 'Roasting' from the Excel file
file_path = 'Bean there done that data.xlsx'
Roasting = pd.read_excel(file_path, sheet_name='Roasting')

# Ensure 'Month' is treated as a categorical type and abbreviated
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
Roasting['Month'] = pd.Categorical(Roasting['Month'], categories=month_order, ordered=True)
Roasting['Month'] = Roasting['Month'].apply(lambda x: x[:3])

# Filter the data for 'Medium roast'
filtered_data = Roasting[Roasting['Product type'] == 'Light Roast']

# Plot the area chart with 'Load weight p/batch' limited by 'Final weight /pbatch'
plt.figure(figsize=(10, 6))
plt.fill_between(filtered_data['Month'], filtered_data['Final weight /pbatch'], 
                 filtered_data['Load weight p/batch'], color='orangered', alpha=0.8)

# Set y-axis limits from 0 to 60
plt.ylim(0, 125)

# Set x-axis limits based on the index of the filtered data
plt.xlim(filtered_data['Month'].min(), filtered_data['Month'].max())

# Remove x-axis and y-axis labels
plt.gca().set_xlabel('')
plt.gca().set_ylabel('')

# Remove the legend
plt.legend().set_visible(False)

# Remove the right y-axis and the top x-axis
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Get December data
december_data = filtered_data[filtered_data['Month'] == 'Dec']

# Calculate max and min values for December
max_value_dec = december_data['Load weight p/batch'].max()
min_value_dec = december_data['Final weight /pbatch'].min()

# Get the position for December
december_index = filtered_data['Month'].tolist().index('Dec')

# Add labels at the max and min values for December
plt.text(december_index + 0.1, max_value_dec - 0.3, 'Loaded', 
         color='black', va='bottom', ha='left', fontsize=12)
plt.text(december_index + 0.1, min_value_dec + 0.3, 'Final', 
         color='black', va='top', ha='left', fontsize=12)

# Add y-axis labels on the right side
plt.gca().yaxis.tick_left()
plt.gca().yaxis.set_label_position("left")

# Add titles to the left
plt.text(-0.035, 1.02, 'Weight Loss', color='orangered', weight='bold', fontsize=16, transform=plt.gca().transAxes)
plt.text(0.15, 1.02, 'Light Roast (in kg)', color='black', weight='bold', fontsize=16, transform=plt.gca().transAxes)

# Calculate the average percentage of fill-between
average_fill_between = ((filtered_data['Load weight p/batch'] - filtered_data['Final weight /pbatch']) / filtered_data['Load weight p/batch']).mean() * 100

# Add average percentage text in the middle of the fill-between and adjust its position
average_fill_between = ((filtered_data['Load weight p/batch'] - filtered_data['Final weight /pbatch']) / filtered_data['Load weight p/batch']).mean() * 100
middle_index = len(filtered_data) // 2

# Calculate the y-position using the average of the fill between values
y_position = (filtered_data['Load weight p/batch'].iloc[middle_index] + filtered_data['Final weight /pbatch'].iloc[middle_index]) / 2

# Set the x-position using the month labels instead of the index
x_position = filtered_data['Month'].iloc[middle_index]

plt.text(x_position, y_position, f'{average_fill_between:.1f}%', color='black', va='center', ha='center', fontsize=16, weight='bold')


# Show the plot
plt.tight_layout()
plt.show()