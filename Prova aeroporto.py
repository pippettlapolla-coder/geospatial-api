import math
import csv
import folium
class Aeroporto:
    def __init__(self,nome,codice,lat,lon,paese,continente):
        self.nome=nome
        self.codice=codice
        self.lat=lat
        self.lon=lon
        self.paese=paese
        self.continente=continente

    def info(self):
        print(f'{self.nome}: {self.codice} | {self.lat}, {self.lon} | {self.paese},{self.continente}')
    def distanza(self,altro):
        R=6371
        lat1=math.radians(self.lat)
        lon1=math.radians(self.lon)
        lat2=math.radians(altro.lat)
        lon2=math.radians(altro.lon)
        dlat=lat2-lat1
        dlon=lon2-lon1
        a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return round(R*c,2)
aeroporti = [
    Aeroporto("Fiumicino", "FCO", 41.7999, 12.2462,'Italy','Europe'),
    Aeroporto("Heathrow", "LHR", 51.4700, -0.4543,'England','Europe'),
    Aeroporto("JFK", "JFK", 40.6413, -73.7781,'USA','North America'),
    Aeroporto("Narita", "NRT", 35.7719, 140.3929,'Japan','Asia'),
    Aeroporto("Sydney", "SYD", -33.9399, 151.1753,'Australia','Australia')
]
def salva_csv(file_nome,lista_aeroporti):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['nome','codice','lat','lon','paese','continente'])
        for a in lista_aeroporti:
            writer.writerow([a.nome, a.codice, a.lat,a.lon,a.paese,a.continente])
def carica_csv(file_nome):
    lista=[]
    with open(file_nome,'r')as file:
        reader=csv.reader(file)
        next(reader)
        for riga in reader:
             nome,codice,lat,lon,paese,continente=riga 
             lista.append(Aeroporto(nome,codice,float(lat),float(lon),paese,continente))
       
    return lista
def calcola_distanza(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            a1=lista[i]
            a2=lista[j]
            dist=a1.distanza(a2)
            print(f'{a1.codice}→{a2.codice} : {dist} KM')
def crea_mappa(lista,file_mappa='mappa_aeroporti.html'):
    m=folium.Map(location=[20,0],zoom_start=2)
    for a in lista:
        folium.Marker([a.lat,a.lon], popup=f'{a.nome} ({a.codice},{a.paese})').add_to(m)
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            a1=lista[i]
            a2=lista[j]
            folium.PolyLine([(a1.lat,a1.lon),(a2.lat,a2.lon)],color='red').add_to(m)
    m.save(file_mappa)
    print(f'Mappa salvata in {file_mappa}')
colori_continente = {
    'Europe': 'blue',
    'Asia': 'green',
    'North America': 'red',
    'South America': 'orange',
    'Africa': 'purple',
    'Australia': 'darkred',
    'Antarctica': 'lightblue'
}

def crea_mappa_colorata(lista, file_mappa='mappa_aeroporti_colorata.html'):
    # Creo la mappa
    m = folium.Map(location=[20,0], zoom_start=2)
    
    # Aggiungo i marker con colore in base al continente
    for a in lista:
        colore = colori_continente.get(a.continente, 'gray')  # default grigio se non trovato
        folium.CircleMarker(
            location=[a.lat, a.lon],
            radius=7,
            color=colore,
            fill=True,
            fill_color=colore,
            fill_opacity=0.7,
            popup=f"{a.nome} ({a.codice})\n{a.paese}, {a.continente}"
        ).add_to(m)
    
    # Linee tra aeroporti (opzionale, colore neutro)
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            a1 = lista[i]
            a2 = lista[j]
            folium.PolyLine(
                [(a1.lat, a1.lon), (a2.lat, a2.lon)],
                color='gray',
                weight=1,
                opacity=0.5
            ).add_to(m)
    
    # Salvo mappa
    m.save(file_mappa)
    print(f"Mappa salvata in {file_mappa}")
salva_csv('aeroporti.csv', aeroporti)
lista=carica_csv('aeroporti.csv')
calcola_distanza(lista)
crea_mappa(lista)
import webbrowser
webbrowser.open('mappa_aeroporti.html')

import os

import webbrowser
import webbrowser

# Specifico il browser (Chrome)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open(r"C:\Users\Lapol\Desktop\mappa_aeroporti_colorata.html")



