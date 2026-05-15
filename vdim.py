import os
import webbrowser
import csv
import math
import folium

class Citta:
    def __init__(self,citta,abitanti,stato,continente,lat,lon):
        self.citta=citta
        self.abitanti=abitanti
        self.stato=stato
        self.continente=continente
        self.lat=lat
        self.lon=lon
    def info(self):
        print(f'{self.citta} ha {self.abitanti} e si trova in {self.continente} | {self.lat},{self.lon}')

    def distanza(self,altro):
        R=6371
        lat1,lon1=math.radians(self.lat),math.radians(self.lon)
        lat2,lon2=math.radians(altro.lat),math.radians(altro.lon)
        dlat=lat2-lat1
        dlon=lon2-lon1
        a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.asin(math.sqrt(a))
        return round(R*c,2)
lista_citta=[
    Citta('Tokyo', 37400000, 'Giappone','Asia',35.6895,139.6917),
    Citta('New York',8300000,'USA','America',40.7128,-74.0060),
    Citta('San Paolo', 20000000,'Barisle','America', -23.5505,-46.6333),
    Citta('Cairo',10000000,'Egitto','Africa', 30.0444,31.2357),
    Citta('Sydney',5300000,'Australia','Oceania',-33.8688,151.2093),
    Citta('Parigi',2300000,'Francia','Europa',48.8566,2.3522),
    Citta('Mumbai',20000000,'India','Asia',19.0760,72.8777),
    Citta('Cape Town',4600000,'Sud Africa','Africa',-33.9249,18.4241),
    Citta('Honk Hong', 7500000,'Honk Hong','Asia',22.3964,114.1095)
]


def salva_csv(file_nome,lista_citta):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['citta','abitanti','stato','continente','lat','lon'])
        for c in lista_citta:
            writer.writerow([c.citta,c.abitanti,c.stato,c.continente,c.lat,c.lon])
def carica_csv(file_nome):
    lista=[]
    with open(file_nome,'r')as file:
        reader=csv.reader(file)
        next(reader)
        for citta,abitanti,stato,continente,lat,lon in reader:
            lista.append(Citta(citta,int(abitanti),stato,continente,float(lat),float(lon)))
    return lista
def trova_citta(lista,nome):
    nome_lower=nome.lower().strip()
    for citta in lista:
        if citta.citta.lower()==nome_lower:
            return citta
    return None
def elenca_citta(lista):
    print("\n" + "="*60)
    print("CITTA DISPONIBILI:")
    print("="*60)
    for i, citta in enumerate(lista, 1):
        print(f"{i}. {citta.citta:20} - {citta.stato:15} ({citta.continente})")
    print("="*60 + "\n")
def calcola_distanza(lista):
    elenca_citta(lista)
    while True:
        print(f'\nInserisci la prima città')
        citta1=input('>').lower().strip()
        if citta1.lower()=='indietro':
            return
        citta1=trova_citta(lista,citta1)
        if not citta1:
            print(f'\nErrore, città non trovata!')
            continue
        print(f'\nCittà {citta1.citta} selezionata')

        print(f'\nInserisci il nome della seconda città')
        citta2=input('>').lower().strip()
        citta2=trova_citta(lista,citta2)
        if not citta2:
            print('\nErrore, città non presente')
            continue
        print(f'\nCittà {citta2.citta} selezionata')
        distanza=citta1.distanza(citta2)
        print("\n" + "="*60)
        print(f"DISTANZA TRA {citta1.citta} E {citta2.citta}:")
        print(f"📍 {distanza} KM")
        print("="*60 + "\n")
        
        continua = input("Vuoi calcolare un'altra distanza? (s/n): ").strip().lower()
        if continua != 's':
            return
def calcola_tutte_distanze(lista):
    print("\n" + "="*60)
    print("DISTANZE TRA TUTTE LE CITTA':")
    print("="*60 + "\n")
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            a1,a2=lista[i],lista[j]
            dist=a1.distanza(a2)
            print(f"{a1.citta:20} - {a2.citta:20}: {dist:6.2f} KM")
    print()
def crea_mappa(lista,file_mappa='mappa_citta.html'):
    m=folium.Map(
        location=[20,0],
        zoom_start=2,
        tiles='OpenStreetMap'
        )
    for c in lista:
        folium.Marker([c.lat,c.lon],popup=f"<b>{c.citta}</b><br>{c.stato}<br>{c.continente}<br>{c.abitanti}").add_to(m)
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            c1,c2=lista[i],lista[j]
            dist=c1.distanza(c2)
            folium.PolyLine(
                [(c1.lat,c1.lon),(c2.lat,c2.lon)],
                color='Grey',
                popup=f"{dist} KM"
            ).add_to(m)
            mid_lat=(c1.lat+c2.lat)/2
            mid_lon=(c1.lon+c2.lon)/2
            folium.Marker(
                [mid_lat,mid_lon],
                icon=folium.DivIcon(
                    html=f"<div style='font-size: 10pt; color:black;'>{dist} km</div>"
                )
            ).add_to(m)
    m.save(file_mappa)
    print(f"Mappa salvata in {file_mappa}")
def aggiungi_citta(lista):
    print("\n"+'='*60)
    print(' AGGIUNGI UNA NUOVA CITTA')
    print('='*60)
    citta=input("Nome Città: ").strip()
    abitanti=int(input('Abitanti Città: ').strip())
    stato=input('Stato Città: ').strip()
    continente=input('Continente Città: ').strip()
    lat=float(input('Lat Città: ').strip())
    lon=float(input('Lon Città: ').strip())
    nuova_citta=Citta(citta,abitanti,stato,continente,lat,lon)
    lista.append(nuova_citta)
    print(f'\nCittà inserita correttamente nel manager')
    salva_csv('citta.csv',lista)
    print('Dati salvati correttamente!')
    return lista

def menu_principale(lista):
    while True:
        print("\n"+'='*60)
        print('MANAGER CITTA')
        print('='*60)
        print("1. Calcola distanza tra due città")
        print("2. Visualizza tutte le distanze")
        print("3. Elenca tutte le città")
        print("4. Crea mappa")
        print("5. Aggiungi una città")
        print("6. Esci")
        scelta=input(f"\nScegli un'opzione (1-6)").strip()
        if scelta=='1':
            calcola_distanza(lista)
        elif scelta=='2':
            calcola_tutte_distanze(lista)
        elif scelta=='3':
            elenca_citta(lista)
        elif scelta=='4':
            crea_mappa(lista)
            apri=input('Aprire la mappa nel browser? (s/n):').strip().lower()
            if apri=='s':
                webbrowser.open(os.path.abspath('mappa_citta.html'))
        elif scelta=='5':
            lista=aggiungi_citta(lista)
        elif scelta=='6':
            print('Arrivederci')
            break
        else:
            print('Opzione non valida, riprova.')

if __name__=='__main__':
    salva_csv('citta.csv',lista_citta)
    citta_caricate=carica_csv('citta.csv')
    menu_principale(citta_caricate)



        





 