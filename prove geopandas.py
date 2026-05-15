
import geopandas as gpd
from shapely.geometry import Point
luoghi=[
    {'nome':'Roma', 'lat':41.9, 'long': 12.5},
    {'nome': 'Milano', 'lat': 45.5, 'long': 9.2},
    {'nome':'Napoli', 'lat': 40.8, 'lon':14.2}
]

gdf=gpd.GeoDataFrame(
    luoghi, 
    gemotry=[Point(l['lon'], l['lat'])for l in luoghi],
    crs='EPSG:4326'
)
print(gdf)
from shapely.geometry import Point
roma=Point(12.5,41.9)
gdf['Distanza da Roma']=gdf.geometry.distance(roma)*111
vicini=gdf[gdf['distanza da Roma']<=400]
print(vicini[['nome', 'distanza da Roma']])