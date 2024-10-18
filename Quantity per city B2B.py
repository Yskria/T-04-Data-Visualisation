
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Bestandsnaam van de Excel
Bean_there = 'Bean there done that data.xlsx'

# Lees het specifieke tabblad in
df_tab5 = pd.read_excel(Bean_there, sheet_name='B2B orders')

# Groepeer op City en sommeer de hoeveelheden (Quantity) per stad
df_city_Quantitys = df_tab5.groupby('City')['Quantity'].sum().reset_index()

# Hernoem de kolommen voor duidelijkheid
df_city_Quantitys.columns = ['City', 'Total Quantity']

# Sorteer de steden op basis van de totale hoeveelheid, van laag naar hoog
df_city_Quantitys = df_city_Quantitys.sort_values(by='Total Quantity', ascending=True)

# Maak een lijst met kleuren, waarbij 'red' wordt gebruikt voor Total Quantity < 1000, 'salmon' voor Total Quantity < 2000, en 'lightgrey' voor de rest
colors = ['red' if qty < 1000 else 'salmon' if qty < 2000 else 'lightgrey' for qty in df_city_Quantitys['Total Quantity']]

# Maak een barplot om de totale hoeveelheid per stad te visualiseren
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Quantity', y='City', data=df_city_Quantitys, palette=colors)  # Gebruik de aangepaste kleurenlijst

# Voeg titels en labels toe
plt.title('B2B Total Quantity per City', fontsize=21, weight='bold', loc='left', pad=10, x=-0.22)  # Plaats titel linksboven met padding en schuif naar links

# Verwijder de titels van de x-as en y-as
plt.xlabel('')  # Lege string voor x-as titel
plt.ylabel('')  # Lege string voor y-as titel

# Maak de y-as labels groter
plt.yticks(fontsize=14)  # Pas de fontsize aan voor y-as labels
plt.xticks(fontsize=14)

# Verwijder de zwarte rand om de visualisatie heen
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Voeg een formatter toe aan de x-as om duizendtallen als 'k' weer te geven, zonder 'k' bij 0
def thousands_formatter(x, pos):
    if x == 0:
        return '0'
    else:
        return '%1.0fk' % (x * 1e-3)

plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# Voeg een verticale stippellijn toe bij 2k
plt.axvline(x=2000, color='grey', linestyle=':', linewidth=1.5)

# Toon de plot
plt.tight_layout()
plt.show()

#Improvement opportunitie: remove city's with 1 Quantity per city to focus on B2B Quantitys nearby.
#Growth: focus on city's with 1 or 2 Quantitys to grow in those city's. In that case you don't drive to a city for one Quantity.

