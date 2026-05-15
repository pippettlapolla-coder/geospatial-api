import math
import folium
import csv
from shapely.geometry import Point
class Citta:
    def __init__(self,nome,lat,lon):
        self.nome=nome
        self.lat=lat
        self.lon=lon
    def info(self):
        print(f'{self.nome} : ({self.lat}, {self.lon})')
    def distanza(self,altra_citta):
        R=6371
        lat1=math.radians(self.lat)
        lon1=math.radians(self.lon)
        lat2=math.radians(altra_citta.lat)
        lon2=math.radians(altra_citta.lon)
        dlat=lat2-lat1
        dlon=lon2-lon1
        a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        return round(R*c,2)
citta_mondo=[
    Citta('Roma',41.9028, 12.4964),
    Citta("Tokyo", 35.6895, 139.6917),
    Citta("New York", 40.7128, -74.0060),
    Citta("Sydney", -33.8688, 151.2093),
    Citta("Rio de Janeiro", -22.9068, -43.1729)
]
def salva_citta_csv(file_nome,lista_citta):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['nome','lat','lon'])
        for c in lista_citta:
            writer.writerow([c.nome, c.lat, c.lon])
def carica_citta_csv(file_nome):
    lista=[]
    with open(file_nome,'r')as file:
        reader=csv.reader(file)
        next(reader)
        for riga in reader:
            nome,lat,lon=riga
            lista.append(Citta(nome,float(lat),float(lon)))
    return lista
def calcola_distanza(lista_citta):
    for i in range(len(lista_citta)):
        for j in range(i+1,len(lista_citta)):
            c1=lista_citta[i]
            c2=lista_citta[j]
            dist=c1.distanza(c2)
            print(f"Distanza {c1.nome} – {c2.nome}: {dist} km")
def crea_mappa(lista_citta, file_mappa='mappa_citta.html'):
    m=folium.Map(location=[0,0],zoom_start=2)
    for c in lista_citta:
        folium.Marker([c.lat,c.lon], popup=c.nome).add_to(m)
    for i in range(len(lista_citta)):
        for j in range(i+1,len(lista_citta)):
            c1=lista_citta[i]
            c2=lista_citta[j]
            folium.PolyLine([(c1.lat,c1.lon),(c2.lat,c2.lon)],color='blue').add_to(m)
    m.save(file_mappa)
    print(f'Mappa salvata in {file_mappa}')
# salva città in CSV
salva_citta_csv("citta_mondo.csv", citta_mondo)

# carica città
lista = carica_citta_csv("citta_mondo.csv")

# calcola distanze
calcola_distanza(lista)

# crea mappa
crea_mappa(lista)
import webbrowser

webbrowser.open("mappa_citta.html")






