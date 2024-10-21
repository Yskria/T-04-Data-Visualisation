import pandas as pd
import matplotlib.pyplot as plt

# Bestandsnaam van de Excel
Bean_there = 'Bean there done that data.xlsx'

# Lees alleen tabblad 4 en 5 in
df_tab4 = pd.read_excel(Bean_there, sheet_name='E-com sales orders by product')
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Zorg ervoor dat 'Delivery date' correct als datetime wordt geïnterpreteerd
df_tab4['Delivery date'] = pd.to_datetime(df_tab4['Delivery date'])
df_tab5['Delivery date'] = pd.to_datetime(df_tab5['Delivery date'])

# Filter alleen de "Medium Roast" rijen voor e-com sales (pas de kolomnaam aan op basis van je data)
df_tab4_medium_roast = df_tab4[df_tab4['Product'] == 'Medium Roast']  # Pas de kolom 'Product' aan indien nodig

# Voeg de kolom 'Profit E-com sales' toe aan de gefilterde dataset voor e-com sales
if all(col in df_tab4_medium_roast.columns for col in ['Value', 'Shipping costs', 'Delivery fee', 'Quantity', 'Bag type']):
    # Conditionele aanpassing voor de 'Quantity' als 'Bag type' 1 is
    df_tab4_medium_roast['Adjusted Quantity'] = df_tab4_medium_roast.apply(
        lambda row: row['Quantity'] * 2 if row['Bag type'] == 1 else row['Quantity'], axis=1
    )
    
    # Berekening van de winst, waarbij de 'Adjusted Quantity' wordt gebruikt
    df_tab4_medium_roast['Profit E-com sales'] = (
        (df_tab4_medium_roast['Value'] + df_tab4_medium_roast['Shipping costs'] + df_tab4_medium_roast['Delivery fee'])
        / df_tab4_medium_roast['Adjusted Quantity']
    )

# Voeg de kolom 'Profit B2B orders' toe aan tabblad 5
if all(col in df_tab5.columns for col in ['Value', 'Shipping costs', 'Quantity']):
    df_tab5['Profit B2B orders'] = (df_tab5['Value'] + df_tab5['Shipping costs']) / df_tab5['Quantity']

# Filter alleen data uit 2023 voor beide datasets
df_tab4_medium_roast = df_tab4_medium_roast[df_tab4_medium_roast['Delivery date'].dt.year == 2023]
df_tab5 = df_tab5[df_tab5['Delivery date'].dt.year == 2023]

# Bereken het gemiddelde over heel 2023 voor beide datasets
mean_profit_ecom = df_tab4_medium_roast['Profit E-com sales'].mean()
mean_profit_b2b = df_tab5['Profit B2B orders'].mean()

# Maak een lijst met de gemiddelde winst per categorie
categories = ['Average Profit (2023)']
mean_b2b = [mean_profit_b2b]
mean_ecom = [mean_profit_ecom]

# Maak de stacked bar chart horizontaal
plt.figure(figsize=(12, 3))

# Stacked bar chart met B2B orders onder en E-com sales bovenop
plt.barh(categories, mean_b2b, label='B2B orders', color='cornflowerblue')
plt.barh(categories, mean_ecom, left=mean_b2b, label='E-com sales (Medium Roast)', color='lightgrey')

# Instellingen van de grafiek
title_text = "ARPU (€) in B2B sales tops E-com in '23 | Medium Roast"
first_part = ' '.join(title_text.split()[:5])  # De eerste vier woorden
remaining_part = ' '.join(title_text.split()[5:])  # De rest van de titel

# Plaats de titel met gescheiden kleuren
plt.text(0, 1.1, first_part, fontsize=22, fontweight='bold', color='cornflowerblue', transform=plt.gca().transAxes)  # Eerste 4 woorden
plt.text(0.33, 1.1, remaining_part, fontsize=22, fontweight='bold', color='black', transform=plt.gca().transAxes)  # Rest van de titel

# Verhoog het lettertype van de ticks
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)

# Verwijder de y-as en x-as labels
plt.ylabel('')  # Verwijder de y-as label
plt.xlabel('')  # Verwijder de x-as label

# Verwijder de y-as ticks (categorieën)
plt.yticks([])

# Verwijder de lijn van de y-as
plt.gca().spines['left'].set_visible(False)

# Verwijder de legenda
# plt.legend()  # Deze regel is nu verwijderd

# Verwijder de grid op de achtergrond
plt.grid(False)

# Verander de dikte van de randen
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Toon de grafiek
plt.tight_layout()
plt.show()
