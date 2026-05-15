import pandas as pd
import numpy as np

data = {
    "zona": ["A", "A", "B", "B", "C", "C", "A", "B"],
    "temperatura": [30, 32, 28, 35, 25, 27, 31, 33],
    "pioggia": [100, 80, 60, 120, 90, 110, 95, 70],
    "altitudine": [200, 250, 100, 150, 300, 350, 220, 130]
}

df = pd.DataFrame(data)
df['indice_climatico']=df['temperatura']/df['pioggia']
df['critico']=(df['temperatura']>30) & (df['pioggia']<90)
df['filtro']=df['critico'] & (df['altitudine']>150)
statistiche=df.groupby('zona').agg({
    'temperatura':'mean',
    'pioggia':'max',
    'altitudine':'min'
}).rename(columns={
    'temperatura':'temp_media',
    'pioggia':'pioggia_max',
    'altitudine':'altitudine_min'
})
df['media_zona']=df.groupby('zona')['temperatura'].transform('mean')
df['deviazione']=df['temperatura']-df['media_zona']
idx=df.groupby('zona')['temperatura'].idxmax()
top=df.loc[idx]
df['livello_temp']=np.where(df['temperatura']>=33,'alto',
                    np.where(df['temperatura']>=29,'medio','basso'))
df_sorted=df.sort_values(by=['zona','temperatura'],ascending=[True,False])
df['rischio']=(
               (df['temperatura']>30)&
               (df['pioggia']<100)&
               (df['altitudine']>200)
)
df['rank_temp']=df.groupby('zona')['temperatura'].rank(method='dense',ascending=False)
df['perc_max']=df['temperatura']/df.groupby('zona')['temperatura'].transform('max')
df['zscore']=(
    (df['temperatura']- df.groupby('zona')['temperatura'].transform('mean'))/
              df.groupby('zona')['temperatura'].transform('std')
)
df_caldo=df.groupby('zona').filter(lambda x: x['temperatura'].mean()>30)
pivot=df.pivot_table(
    values='temperatura',
    index='zona',
    aggfunc=['mean','max','min']
)
df=df.merge(statistiche, on='zona')
print(df)
