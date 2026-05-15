import math
import csv
import folium

class Stadio:
    def __init__(self,nome,squadra,citta,lat,lon):
        self.nome=nome
        self.squadra=squadra
        self.citta=citta
        self.lat=lat
        self.lon=lon
    def distanza(self,altro):
        R=6371
        lat1=math.radians(self.lat)
        lon1=math.radians(self.lon)
        lat2=math.radians(altro.lat)
        lon2=math.radians(altro.lon)
        dlat=lat2-lat1
        dlon=lon2-lon1
        a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        return round(R*c,2)
    def info(self):
        print(f'{self.nome} stadio della squadra {self.squadra}, ubicato a {self.citta} ha le seguenti coordinate: {self.lat}, {self.lon}')
Stadi=[
    Stadio('San_Siro', 'Milan/Inter', 'Milano', 45.4781, 9.1239),
    Stadio('Olimpico','Lazio/Roma','Roma', 41.9336, 12.4546),
    Stadio('Allianz','Juventus','Torino', 45.1094, 7.6411),
    Stadio('Artemio Franchi','Fiorentina','Firenze', 43.8070, 11.2587),
    Stadio('Maradona','Napoli','Napoli', 40.8359, 14.2463),
    Stadio('Dall_Ara','Bologna','Bologna', 44.4950, 11.3390),
    Stadio('Ferraris','Genoa','Genova', 44.4962, 8.9333),
    Stadio('Friuli','Udinese','Udine', 46.0650, 13.2340),
    Stadio('Gewiss','Atalanta','Bergamo', 45.6895, 9.6773),
    Stadio('Curi','Perugia','Perugia', 43.0953, 12.5741),
    Stadio('San_Nicola','Bari','Bari', 41.0842, 16.8374)
]
def salva_csv(file_nome,lista_stadi):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['nome','squadra','citta','lat','lon'])
        for s in lista_stadi:
            writer.writerow([s.nome,s.squadra,s.citta,s.lat,s.lon])
def carica_csv(file_nome):
    lista=[]
    with open(file_nome,'r')as file:
        reader=csv.reader(file)
        next(reader)
        for riga in reader:
            nome,squadra,citta,lat,lon=riga
            lista.append(Stadio(nome,squadra,citta,float(lat),float(lon)))
    return lista
def calcola_distanza(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            a1=lista[i]
            a2=lista[j]
            dist=a1.distanza(a2)
            print(f'{a1.nome} - {a2.nome}: {dist} KM')

def crea_mappa(lista,file_mappa='mappa_stadi.html'):
    m=folium.Map(location=[43,12], zoom_start=6)
    for s in lista:
        folium.Marker([s.lat,s.lon], popup=f"<b>{s.nome}</b><br>{s.squadra}<br>{s.citta}").add_to(m)
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            s1=lista[i]
            s2=lista[j]
            dist=s1.distanza(s2)
            if dist<200:
                folium.PolyLine([(s1.lat,s1.lon),(s2.lat,s2.lon)], color='red').add_to(m)  
            mid_lat = (s1.lat + s2.lat) / 2
            mid_lon = (s1.lon + s2.lon) / 2

            # etichetta distanza
            folium.Marker(
                [mid_lat, mid_lon],
                icon=folium.DivIcon(html=f"""
                    <div style="font-size: 10pt; color: black;">
                    {dist} km
                    </div>
                    """)
                ).add_to(m)
    m.save(file_mappa)
    print(f'Mappa salvata in {file_mappa}')
salva_csv('stadi.csv', Stadi)

# carica i dati da CSV
stadi_caricati = carica_csv('stadi.csv')

# calcola e stampa tutte le distanze
calcola_distanza(stadi_caricati)

# crea la mappa
crea_mappa(stadi_caricati)

# apri la mappa
import webbrowser
import os
file_mappa = os.path.abspath('mappa_stadi.html')
webbrowser.open(file_mappa)




    

    