import geopandas as gpd 
from shapely.geometry import Point
import matplotlib.pyplot as plt
citta={
    'nome':['Roma','Milano','Napoli','Firenze','Bologna'],
    'lat':[41.9,45.46,40.85,43.77,44.49],
    'lon':[12.5,9.19,14.27,11.25,11.34]
}
geometry=[Point(xy)for xy in zip(citta['lon'],citta['lat'])]
gdf=gpd.GeoDataFrame(citta,geometry=geometry, crs='EPSG:4326')
print(gdf)
gdf=gdf.to_crs(epsg=3857)
roma=gdf[gdf['nome']=='Roma'].geometry.iloc[0]
gdf['distanza_da_Roma']=gdf.geometry.distance(roma)
altre_citta=gdf[gdf['nome']!='Roma']
piu_vicina=altre_citta.loc[altre_citta['distanza_da_Roma'].idxmin()]
print('La città più vicina a Roma è:', piu_vicina['nome'])
roma=gdf[gdf['nome']=='Roma'].geometry.iloc[0]
buffer_roma=roma.buffer(300000)
citta_nel_raggio=gdf[gdf.geometry.within(buffer_roma)]
print(citta_nel_raggio['nome'])
print(buffer_roma)
buffer_gdf=gpd.GeoDataFrame(geometry=[buffer_roma],crs=gdf.crs)
ax=buffer_gdf.plot(alpha=0.3)
gdf.plot(ax=ax, color='red')
plt.show()