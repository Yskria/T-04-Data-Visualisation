import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Bestandsnaam van de Excel
Bean_there = 'Bean there done that data.xlsx'

# Lees alleen tabblad 4 en 5 in
df_tab4 = pd.read_excel(Bean_there, sheet_name='E-com sales orders by product')
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Zorg ervoor dat 'Delivery date' correct als datetime wordt geïnterpreteerd
df_tab4['Delivery date'] = pd.to_datetime(df_tab4['Delivery date'])
df_tab5['Delivery date'] = pd.to_datetime(df_tab5['Delivery date'])

# Voeg de kolom 'Profit E-com sales' toe aan tabblad 4
if all(col in df_tab4.columns for col in ['Value', 'Shipping costs', 'Delivery fee', 'Quantity']):
    df_tab4['Profit E-com sales'] = (df_tab4['Value'] - df_tab4['Shipping costs'] - df_tab4['Delivery fee']) * df_tab4['Quantity']

# Voeg de kolom 'Profit B2B orders' toe aan tabblad 5
if all(col in df_tab5.columns for col in ['Value', 'Shipping costs', 'Quantity']):
    df_tab5['Profit B2B orders'] = (df_tab5['Value'] - df_tab5['Shipping costs']) * df_tab5['Quantity']

# Filter alleen data uit 2023
df_tab4 = df_tab4[df_tab4['Delivery date'].dt.year == 2023]
df_tab5 = df_tab5[df_tab5['Delivery date'].dt.year == 2023]

# Groepeer per maand om de som van de winst per maand te krijgen
df_tab4['Month'] = df_tab4['Delivery date'].dt.to_period('M')
df_tab5['Month'] = df_tab5['Delivery date'].dt.to_period('M')

df_profit_ecom = df_tab4.groupby('Month')['Profit E-com sales'].sum().reset_index()
df_profit_b2b = df_tab5.groupby('Month')['Profit B2B orders'].sum().reset_index()

# Voeg een kolom toe om de categorieën te onderscheiden
df_profit_ecom['Type'] = 'E-com sales'
df_profit_b2b['Type'] = 'B2B orders'

# Hernoem de kolommen naar een gemeenschappelijke naam voor de y-as
df_profit_ecom.rename(columns={'Profit E-com sales': 'Profit'}, inplace=True)
df_profit_b2b.rename(columns={'Profit B2B orders': 'Profit'}, inplace=True)

# Combineer de twee datasets voor eenvoudige plotten
df_combined = pd.concat([df_profit_ecom, df_profit_b2b], axis=0)

# Maak een pivot table voor de lijndiagram
df_pivot = df_combined.pivot(index='Month', columns='Type', values='Profit').fillna(0)

# Converteer de 'Month' Period naar een integer representatie van de maand
df_pivot.index = df_pivot.index.astype(str).str[-2:].astype(int)  # Neem alleen de maand als integer

# Voeg de voorspelling voor 2024 toe met een stijging van 10%
df_pivot_2024 = df_pivot.copy() * 1.1
df_pivot_2024.index = df_pivot_2024.index + 12  # Schuif de index op om 2024 weer te geven

# Combineer de 2023 en 2024 datasets
df_pivot_combined = pd.concat([df_pivot, df_pivot_2024])

# Maak het lijndiagram met Matplotlib
plt.figure(figsize=(16, 6))  # Verhoog de breedte naar 16

# Plot de lijnen voor elk type in 2023 (zonder markers en met gelijke lijndikte)
plt.plot(df_pivot.index, df_pivot['E-com sales'], label='E-com sales 2023', linewidth=4, color='blue')
plt.plot(df_pivot.index, df_pivot['B2B orders'], label='B2B orders 2023', linewidth=4, color='purple')

# Plot de voorspelde lijnen voor 2024 (met gestreepte lijnen)
plt.plot(df_pivot_2024.index, df_pivot_2024['E-com sales'], label=' E-com sales', linewidth=4, color='blue', linestyle='--')
plt.plot(df_pivot_2024.index, df_pivot_2024['B2B orders'], label=' B2B orders', linewidth=4, color='purple', linestyle='--')

# Voeg een verticale grijze stippellijn toe op de overgang van 2023 naar 2024
plt.axvline(x=12.5, color='grey', linestyle='--', linewidth=2)

# Aangepaste formatter om 'M' toe te voegen, maar niet bij 0
def millions_formatter(x, pos):
    if x == 0:
        return '0'
    return f'{int(x / 1_000_000)}M'

# Formatter voor de y-as om de waarden in hele getallen (miljoenen) weer te geven
plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

# Voeg de lijnlabels handmatig toe (rechts van de voorspellingslijnen) met dikgedrukt lettertype
plt.text(df_pivot_2024.index[-1] + 0.1, df_pivot_2024['E-com sales'].iloc[-1], ' E-com sales', color='blue', 
         ha='left', va='center', fontsize=18, fontweight='bold')
plt.text(df_pivot_2024.index[-1] + 0.1, df_pivot_2024['B2B orders'].iloc[-1], ' B2B orders', color='purple', 
         ha='left', va='center', fontsize=18, fontweight='bold')

# Instellingen van de grafiek
plt.title('Total Profit per Month for E-com Sales and B2B Orders (2023 & Forecast 2024)', loc='left', fontsize=22, fontweight='bold', x=-0.05)  # Titel verder naar links
plt.xlabel('', fontsize=18)  # Lege string voor x-as label
plt.ylabel('Total Profit in €', fontsize=18)

# Verander de labels voor de x-as om leidende nullen weer te geven en na 12 bij 01 te starten
plt.xticks(df_pivot_combined.index, labels=[f'{m:02}' if m <= 12 else f'{m - 12:02}' for m in df_pivot_combined.index], fontsize=12)

# Voeg de jaartallen één keer toe onder de maanden december 2023 en december 2024
plt.text(7, -0.5e6, '2023', ha='center', va='top', fontsize=18, color='black', fontweight='bold')  # Jaartal voor 2023
plt.text(19, -0.5e6, '2024', ha='center', va='top', fontsize=18, color='black', fontweight='bold')  # Jaartal voor 2024

# Vergroot het lettertype van de y-as ticks
plt.tick_params(axis='y', labelsize=15)  # Groter lettertype voor y-as ticks
plt.tick_params(axis='x', labelsize=15)  # Groter lettertype voor x-as ticks

# Verwijder de grid op de achtergrond
plt.grid(False)

# Verander de dikte van de randen
plt.gca().spines['left'].set_linewidth(4)  # Dikte van de linker rand
plt.gca().spines['bottom'].set_linewidth(4)  # Dikte van de onderste rand
plt.gca().spines['top'].set_visible(False)  # Bovenste rand verbergen
plt.gca().spines['right'].set_visible(False)  # Rechte rand verbergen

# Toon de grafiek
plt.tight_layout()
plt.show()