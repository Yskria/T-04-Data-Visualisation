# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:04:00 2024

@author: Aron Wolswinkel
"""

import pandas as pd

# Bestandsnaam van de Excel
Bean_there = '/Users/Aron Wolswinkel/Downloads/Bean there done that data.xlsx'

# Lees het specifieke tabblad in
df_tab1 = pd.read_excel(Bean_there, sheet_name='Inventory (raw material)')  # Vervang 'Tabblad1' door de naam van je eerste tabblad
df_tab2 = pd.read_excel(Bean_there, sheet_name='Inventory (finished product)')  # Vervang 'Tabblad2' door de naam van je tweede tabblad
df_tab3 = pd.read_excel(Bean_there, sheet_name='Roasting')
df_tab4 = pd.read_excel(Bean_there, sheet_name='E-com sales orders by product')
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')


# Bekijk de eerste paar rijen van een tabblad
print(df_tab1.head())
print(df_tab2.head())
print(df_tab3.head())
print(df_tab4.head())
print(df_tab5.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lees de data uit het Excel-bestand (tabblad 5)
Bean_there = '/Users/Aron Wolswinkel/Downloads/Bean there done that data.xlsx'
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Groepeer de data op klant en sommeer de waarde van hun bestellingen
df_customer_total = df_tab5.groupby('Customer')['Value'].sum().reset_index()

# Sorteer de klanten op basis van de totale waarde
df_customer_total = df_customer_total.sort_values(by='Value', ascending=False)

# Maak een barplot om de totale bestelwaarde per klant te visualiseren
plt.figure(figsize=(10, 6))
sns.barplot(x='Value', y='Customer', data=df_customer_total, palette='Blues_d')

# Voeg titels en labels toe
plt.title('Total Order Value per Customer', fontsize=16)
plt.xlabel('Total Value (€)', fontsize=12)
plt.ylabel('Customer', fontsize=12)

# Toon de plot
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lees de data uit het Excel-bestand (tabblad 5)
Bean_there = '/Users/Aron Wolswinkel/Downloads/Bean there done that data.xlsx'
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Groepeer op City en tel het aantal unieke klanten per stad
df_city_customers = df_tab5.groupby('City')['Customer'].nunique().reset_index()

# Hernoem de kolommen voor duidelijkheid
df_city_customers.columns = ['City', 'Customer Count']

# Sorteer de steden op basis van het aantal klanten
df_city_customers = df_city_customers.sort_values(by='Customer Count', ascending=False)

# Maak een barplot om het aantal klanten per stad te visualiseren
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer Count', y='City', data=df_city_customers, palette='viridis')

# Voeg titels en labels toe
plt.title('Number of Customers per City', fontsize=16)
plt.xlabel('Number of Customers', fontsize=12)
plt.ylabel('City', fontsize=12)

# Toon de plot
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lees de data uit het Excel-bestand (tabblad 5)
Bean_there = '/Users/Aron Wolswinkel/Downloads/Bean there done that data.xlsx'
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Groepeer op City en sommeer de order value per stad
df_city_value = df_tab5.groupby('City')['Value'].sum().reset_index()

# Hernoem de kolommen voor duidelijkheid
df_city_value.columns = ['City', 'Total Order Value']

# Sorteer de steden op basis van de totale order value
df_city_value = df_city_value.sort_values(by='Total Order Value', ascending=False)

# Maak een barplot om de totale order value per stad te visualiseren
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Order Value', y='City', data=df_city_value, palette='magma')

# Voeg titels en labels toe
plt.title('Total Order Value per City', fontsize=16)
plt.xlabel('Total Order Value (€)', fontsize=12)
plt.ylabel('City', fontsize=12)

# Toon de plot
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lees de data uit het Excel-bestand (tabblad 5)
Bean_there = '/Users/Aron Wolswinkel/Downloads/Bean there done that data.xlsx'
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Converteer de kolom 'Delivery date' naar datetime-indeling
df_tab5['Delivery date'] = pd.to_datetime(df_tab5['Delivery date'])

# Groepeer de data op basis van Delivery date en sommeer de hoeveelheid (Quantity)
df_quantity_per_date = df_tab5.groupby('Delivery date')['Quantity'].sum().reset_index()

# Maak een lijnplot om de hoeveelheid per bezorgdatum te visualiseren
plt.figure(figsize=(10, 6))
sns.lineplot(x='Delivery date', y='Quantity', data=df_quantity_per_date, marker='o', color='b')

# Voeg titels en labels toe
plt.title('Total Quantity per Delivery Date', fontsize=16)
plt.xlabel('Delivery Date', fontsize=12)
plt.ylabel('Quantity', fontsize=12)

# Draai de x-as labels om ze leesbaar te maken
plt.xticks(rotation=45)

# Toon de plot
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lees de data uit het Excel-bestand (tabblad 5)
Bean_there = '/Users/Aron Wolswinkel/Downloads/Bean there done that data.xlsx'
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Converteer de kolom 'Delivery date' naar datetime-indeling
df_tab5['Delivery date'] = pd.to_datetime(df_tab5['Delivery date'])

# Groepeer de data op basis van Delivery date en sommeer de totale order value (Value)
df_value_per_date = df_tab5.groupby('Delivery date')['Value'].sum().reset_index()

# Maak een lijnplot om de totale order value per bezorgdatum te visualiseren
plt.figure(figsize=(10, 6))
sns.lineplot(x='Delivery date', y='Value', data=df_value_per_date, marker='o', color='green')

# Voeg titels en labels toe
plt.title('Total Order Value per Delivery Date', fontsize=16)
plt.xlabel('Delivery Date', fontsize=12)
plt.ylabel('Total Order Value (€)', fontsize=12)

# Draai de x-as labels om ze leesbaar te maken
plt.xticks(rotation=45)

# Toon de plot
plt.tight_layout()
plt.show()
