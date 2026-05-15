import pandas as pd
import numpy as np

data = {
    "ordine_id": [101,102,103,104,105,106,107,108,109,110],
    "cliente": ["Anna","Luca","Marco","Anna","Giulia","Luca","Marco","Anna","Giulia","Luca"],
    "città": ["Roma","Milano","Roma","Napoli","Milano","Roma","Napoli","Roma","Milano","Napoli"],
    "categoria": ["Tech","Casa","Tech","Sport","Casa","Tech","Sport","Casa","Tech","Sport"],
    "prezzo": [120,80,200,150,90,220,130,70,210,160],
    "quantità": [1,2,1,3,2,1,2,4,1,2],
    "data": pd.to_datetime([
        "2024-01-10","2024-01-12","2024-01-15","2024-02-01","2024-02-05",
        "2024-02-20","2024-03-01","2024-03-10","2024-03-15","2024-03-20"
    ])
}

df = pd.DataFrame(data)

# aggiungiamo qualche valore mancante
df.loc[3, "prezzo"] = np.nan
df.loc[7, "città"] = np.nan


df['fascia_spesa']=np.where(df['prezzo']>200,'alta',
                    np.where(df['prezzo']>=100,'media','bassa'))
df['mese']=df['data'].dt.month
df['prezzo']=df['prezzo'].fillna(
    df.groupby('categoria')['prezzo'].transform('mean')
)
df['città']=df['città'].fillna(
    df.groupby('cliente')['città'].transform(lambda x: x.mode()[0])
)
df['totale']=df['prezzo']*df['quantità']
fatturato_citta=df.groupby('città')['totale'].sum()
ordini=df.groupby('cliente')['ordine_id'].count()
spesa_media=df.groupby('categoria')['totale'].mean()
pivot=df.pivot_table(
    index='cliente',
    columns='categoria',
    values='totale',
    aggfunc='sum'
)
pivot=pivot.fillna(0)
cat=pivot.idxmax(axis=1)
print(df)
print(pivot)
print(cat)