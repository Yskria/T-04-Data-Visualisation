#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:48:00 2024

@author: Tom
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the specific sheet 'Roasting' from the Excel file
file_path = 'Bean there done that data.xlsx'
Roasting = pd.read_excel(file_path, sheet_name='Roasting')

# Month order for both years
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Ensure 'Month' is treated as a categorical type and shorten to 3 letters
Roasting['Month'] = pd.Categorical(Roasting['Month'], categories=month_order, ordered=True)
Roasting['Month'] = Roasting['Month'].apply(lambda x: x[:3])

# Create the 'Weight p/hour' column
Roasting['Weight p/hour'] = (Roasting['Number of batches per day'] * Roasting['Load weight p/batch']) / 8

# Filter the data for 'Medium roast'
filtered_data = Roasting[Roasting['Product type'] == 'Medium roast']

# Group data for 2023, 2024 and 2025, calculating averages for each quarter
pivot_data_2023 = filtered_data.groupby('Month')['Weight p/hour'].sum()
pivot_data_2024 = (pivot_data_2023 * 1 + pivot_data_2023 * 0.1 * (247918.5/264198.5)).rename(index=lambda x: x + ' 24')  # Renaming to indicate 2024
pivot_data_2025 = (pivot_data_2024 * 1 + pivot_data_2024 * 0.1 * (272710.35/288990.35)).rename(index=lambda x: x + ' 25')  # Renaming to indicate 2025

# Calculate quarterly averages for 2023
quarterly_data = {
    'Q1 2023': (pivot_data_2023['Jan'] + pivot_data_2023['Feb'] + pivot_data_2023['Mar']) / 3,
    'Q2 2023': (pivot_data_2023['Apr'] + pivot_data_2023['May'] + pivot_data_2023['Jun']) / 3,
    'Q3 2023': (pivot_data_2023['Jul'] + pivot_data_2023['Aug'] + pivot_data_2023['Sep']) / 3,
    'Q4 2023': (pivot_data_2023['Oct'] + pivot_data_2023['Nov'] + pivot_data_2023['Dec']) / 3,
}

# Calculate quarterly averages for 2024
quarterly_data_2024 = {
    'Q1 2024': (pivot_data_2024['Jan 24'] + pivot_data_2024['Feb 24'] + pivot_data_2024['Mar 24']) / 3,
    'Q2 2024': (pivot_data_2024['Apr 24'] + pivot_data_2024['May 24'] + pivot_data_2024['Jun 24']) / 3,
    'Q3 2024': (pivot_data_2024['Jul 24'] + pivot_data_2024['Aug 24'] + pivot_data_2024['Sep 24']) / 3,
    'Q4 2024': (pivot_data_2024['Oct 24'] + pivot_data_2024['Nov 24'] + pivot_data_2024['Dec 24']) / 3,
}

# Calculate quarterly averages for 2025
quarterly_data_2025 = {
    'Q1 2025': (pivot_data_2025['Jan 24 25'] + pivot_data_2025['Feb 24 25'] + pivot_data_2025['Mar 24 25']) / 3,
    'Q2 2025': (pivot_data_2025['Apr 24 25'] + pivot_data_2025['May 24 25'] + pivot_data_2025['Jun 24 25']) / 3,
    'Q3 2025': (pivot_data_2025['Jul 24 25'] + pivot_data_2025['Aug 24 25'] + pivot_data_2025['Sep 24 25']) / 3,
    'Q4 2025': (pivot_data_2025['Oct 24 25'] + pivot_data_2025['Nov 24 25'] + pivot_data_2025['Dec 24 25']) / 3,
}

# Create a DataFrame directly from all three dictionaries
combined_data = pd.DataFrame({
    'Weight p/hour': list(quarterly_data.values()) + list(quarterly_data_2024.values()) + list(quarterly_data_2025.values())
}, index=list(quarterly_data.keys()) + list(quarterly_data_2024.keys()) + list(quarterly_data_2025.keys()))

# Create figure
plt.figure(figsize=(10, 6))

# Plot the quarterly averages
plt.plot(combined_data.index[:4], combined_data['Weight p/hour'][:4], linewidth=5, color='lightgrey', linestyle='-')  # Q1-Q4 2023 in lightgrey
plt.plot(combined_data.index[3:8], combined_data['Weight p/hour'][3:8], linewidth=5, color='cornflowerblue', linestyle='-')  # Q1-Q4 2024 in mediumseagreen
plt.plot(combined_data.index[7:], combined_data['Weight p/hour'][7:], linewidth=5, color='cornflowerblue', linestyle='-') 

# Add a vertical line between Q4 2023 and Q1 2024
plt.axvline(x=3.5, color='lightgrey', linewidth=1)  # Vertical line with lightgrey color and linewidth 1
plt.axvline(x=7.5, color='lightgrey', linewidth=1)

# Add horizontal lines for Capacity and Occupancy Rate
capacity_line = 215
occupancy_rate_line = 182.75
plt.axhline(y=capacity_line, color='grey', linestyle='--', linewidth=2)
plt.axhline(y=occupancy_rate_line, color='orangered', linestyle='--', linewidth=2)

# Set y-axis limits and set y-ticks in steps of 20
plt.ylim(0, 220)
plt.yticks(range(0, 221, 20))  # Y-axis steps of 20

# Set x-axis limits to match the combined data range
plt.xlim(0, len(combined_data) - 1)

# Add the title using text, aligned slightly to the left
plt.gca().text(-0.045, 1.05, 'Forecast Utilization Probat P60 (in kg/h)', color='black', fontsize=16, weight='bold', transform=plt.gca().transAxes)

# Add labels for the horizontal lines on the right y-axis
plt.text(len(combined_data) - 0.9, capacity_line, 'Capacity', color='grey', va='center', ha='left', fontsize=12, weight='bold')
plt.text(len(combined_data) - 0.9, occupancy_rate_line, 'Occupancy rate', color='orangered', va='center', ha='left', fontsize=12, weight='bold')

# Add label for the Weight p/hour line
plt.text(len(combined_data) - 0.9, combined_data['Weight p/hour'].values[-1], 'Avg weight', color='cornflowerblue', va='center', ha='left', fontsize=12, weight='bold')

# Update x-axis labels to show Q1, Q2, Q3, and Q4 for each year
plt.xticks(range(len(combined_data)), ['Q1', 'Q2', 'Q3', 'Q4', 
                                        'Q1', 'Q2', 'Q3', 'Q4',
                                        'Q1', 'Q2', 'Q3', 'Q4']) 

# Add the year labels below the x-axis in the middle of each year
plt.text(1.5, -18, '2023', ha='center', fontsize=12, color='black', weight='bold')  # Middle of Q1
plt.text(5.5, -18, '2024', ha='center', fontsize=12, color='black', weight='bold')  # Middle van Q2
plt.text(9.5, -18, '2025', ha='center', fontsize=12, color='black', weight='bold')  # Middle van Q3

# Find the first crossing point in 2025
crossing_index = None
for i in range(8, len(combined_data)):
    if combined_data['Weight p/hour'].iloc[i] >= occupancy_rate_line:
        crossing_index = i
        break

# Add a marker at the crossing point if it exists
if crossing_index is not None:
    plt.plot(crossing_index, combined_data['Weight p/hour'].iloc[crossing_index], marker='X', color='red', markersize=14, label='First Crossing 2025')

# Remove top and right spines (axes)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Remove x-axis and y-axis labels
plt.gca().set_xlabel('')
plt.gca().set_ylabel('')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

# Print the combined data for validation
print(combined_data)
