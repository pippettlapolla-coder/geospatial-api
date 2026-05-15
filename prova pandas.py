import pandas as pd
import numpy as np

data = {
    'ordine_id': [1, 2, 3, 4, 5, 6, 7, 8, 8, 10],
    'cliente': ['Mario', 'Luigi', 'Anna', 'Mario', None, 'Anna', 'Luca', 'Luca', 'Luca', 'Giulia'],
    'citta': ['Roma', 'Milano', 'Roma', 'Roma', 'Napoli', None, 'Milano', 'Milano', 'Milano', 'Torino'],
    'prodotto': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Keyboard', 'Laptop', None, 'Laptop', 'Mouse'],
    'prezzo': [1200, 25, 80, None, 20, 75, 1100, 1100, 1100, -10],
    'quantita': [1, 2, 1, 1, None, 3, 1, 1, 1, 5],
    'data_ordine': ['2024-01-10', '2024-01-11', None, '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-16', '2024-01-16', 'not_a_date']
}

df = pd.DataFrame(data)
df.replace('not_a_date',np.nan,inplace=True)
df['data_ordine']=pd.to_datetime(df['data_ordine'],errors='coerce')
df=df[df['prezzo']>=0]
df=df.dropna()
n_nan=df.isnull().sum()
df['totale']=df['prezzo']*df['quantita']
fatturato_cliente=df.groupby('cliente')['totale'].sum().sort_values(ascending=False)
fatturato_citta=df.groupby('citta')['totale'].sum().sort_values(ascending=False)
same_product=df.groupby(['cliente','prodotto']).size().sort_values(ascending=False)
same_product=same_product[same_product>1]
df=df.drop_duplicates(subset=['ordine_id'])
df['classifica_ordini']=np.where(df['totale']>1000,'alto',
                         np.where(df['totale']>500,'medio','basso'))
print(same_product)
