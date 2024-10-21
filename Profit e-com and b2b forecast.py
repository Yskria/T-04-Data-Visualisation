import pandas as pd
import matplotlib.pyplot as plt

# Bestandsnaam van de Excel
Bean_there = 'Bean there done that data.xlsx'

# Lees alleen tabblad 4 (E-com sales orders by product)
df_tab4 = pd.read_excel(Bean_there, sheet_name='E-com sales orders by product')

# Zorg ervoor dat 'Delivery date' correct als datetime wordt geïnterpreteerd
df_tab4['Delivery date'] = pd.to_datetime(df_tab4['Delivery date'])

# Filter de rijen voor 2023
df_tab4_2023 = df_tab4[df_tab4['Delivery date'].dt.year == 2023]

# Voeg de kolom 'Profit E-com sales' toe aan de gefilterde dataset
if all(col in df_tab4_2023.columns for col in ['Value', 'Shipping costs', 'Delivery fee', 'Quantity', 'Bag type']):
    # Conditionele aanpassing voor de 'Quantity' als 'Bag type' 1 is
    df_tab4_2023['Adjusted Quantity'] = df_tab4_2023.apply(
        lambda row: row['Quantity'] * 2 if row['Bag type'] == 1 else row['Quantity'], axis=1
    )
    
    # Berekening van de winst, waarbij de 'Adjusted Quantity' wordt gebruikt
    df_tab4_2023['Profit E-com sales'] = (
        (df_tab4_2023['Value'] + df_tab4_2023['Shipping costs'] + df_tab4_2023['Delivery fee'])
        / df_tab4_2023['Adjusted Quantity']
    )

# Filter voor Light Roast, Medium Roast en Dark Roast
df_light_roast = df_tab4_2023[df_tab4_2023['Product'] == 'Light Roast']
df_medium_roast = df_tab4_2023[df_tab4_2023['Product'] == 'Medium Roast']
df_dark_roast = df_tab4_2023[df_tab4_2023['Product'] == 'Dark Roast']

# Bereken het gemiddelde van de 'Profit E-com sales' per roast type
mean_profit_light_roast = df_light_roast['Profit E-com sales'].mean()
mean_profit_medium_roast = df_medium_roast['Profit E-com sales'].mean()
mean_profit_dark_roast = df_dark_roast['Profit E-com sales'].mean()

# Maak een lijst met de roast types en hun gemiddelde profit
roast_types = ['Light Roast', 'Medium Roast', 'Dark Roast']
mean_profits = [mean_profit_light_roast, mean_profit_medium_roast, mean_profit_dark_roast]

# Maak de bar chart
plt.figure(figsize=(18, 6))

# Horizontale bar chart voor de gemiddelde profit per roast type
plt.barh(roast_types, mean_profits, color=['cornflowerblue', 'cornflowerblue', 'lightgrey'])

# Plaats de titel boven de y-as en uitgelijnd naar links
plt.suptitle("", fontsize=23, fontweight='bold', x=-0.001, ha='left')

# Voeg de gekleurde tekst toe
plt.text(-2.2, 2.9, "Higher ARPU (€) for Light and Medium Roasts", fontsize=23, fontweight='bold', color='cornflowerblue', ha='left', va='top')
plt.text(6.5, 2.9, "Compared to Dark Roast in E-com Sales in '23", fontsize=23, fontweight='bold', color='black', ha='left', va='top')

# Instellingen van de grafiek
plt.xticks(fontsize=19)
plt.yticks(fontsize=18, fontweight='bold')

# Verwijder de grid op de achtergrond
plt.grid(False)

# Verander de dikte van de randen
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['bottom'].set_linewidth(2)

# Toon de grafiek
plt.tight_layout()
plt.show()
