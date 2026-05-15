import math
import csv
import folium
import webbrowser
from shapely.geometry import Point 
def distanza(lat1,lat2,lon1,lon2):
    R=6371
    lat1=math.radians(lat1)
    lat2=math.radians(lat2)
    lon1=math.radians(lon1)
    lon2=math.radians(lon2)
    dlat=lat2-lat1
    dlon=lon2-lon1
    a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    return R*c
def crea_punto(lat,lon):
    return Point(lon,lat)
citta={
    'Napoli':(40.8518,14.2681),
    'Roma':(41.9028,12.4964),
    'Milano':(45.4641,9.1900),
    'Torino':(45.0703,7.6869),
    'Palermo':(38.1157,13.3615)
}
def salva_csv(file_nome):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['citta','lat','lon'])
        for nome, coord in citta.items():
            lat,lon=coord
            writer.writerow([nome,lat,lon])
def carica_csv(file_nome):
    with open(file_nome,'r') as file:
        reader=csv.reader(file)
        next(reader)
        for riga in reader:
            nome=riga[0]
            lat=float(riga[1])
            lon=float(riga[2])
            citta[nome]=(lat,lon)

def salva_distanze(file_nome):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['citta1','citta2','distanza_km'])
        nomi=list(citta.keys())
        for i in range(len(nomi)):
            for j in range(i+1,len(nomi)):
                c1=nomi[i]
                c2=nomi[j]
                lat1,lon1=citta[c1]
                lat2,lon2=citta[c2]
                dist=distanza(lat1,lat2,lon1,lon2)
                dist=round(dist,2)
                writer.writerow([c1,c2,dist])
                print(c1,c2,dist)

def crea_mappa(file_nome):
    mappa= folium.Map(location=[43,12],zoom_start=6)
    for nome,(lat,lon) in citta.items():
        folium.Marker(
            location=[lat,lon],
            popup=nome
        ).add_to(mappa)
    mappa.save(file_nome)
    webbrowser.open(file_nome)
salva_csv('citta.csv')
print('File citta.csv caricato')
carica_csv('citta.csv')
print('File caricato')
salva_distanze('distanze.csv')
print('File distanze.csv caricato')
crea_mappa('mappa_citta.html')


        
            