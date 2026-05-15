import os
import math
import csv
import folium
import webbrowser


class Citta:
    def __init__(self,nome,provincia,regione,lat,lon):
        self.nome=nome
        self.regione=regione
        self.provincia=provincia
        self.lat=lat
        self.lon=lon
    def distanza(self,altro):
        R=6371
        lat1,lon1=math.radians(self.lat),math.radians(self.lon)
        lat2,lon2=math.radians(altro.lat), math.radians(altro.lon)
        dlat=lat2-lat1
        dlon=lon2-lon1
        a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        return round(R*c,2)
    def info(self):
        print(f'{self.nome} | {self.regione} | {self.provincia}, ({self.lat},{self.lon})')

lista_citta=[
    Citta('Gravina in Puglia','Puglia','BA',40.8189,16.4214),
    Citta('Melendugno','Puglia','LE',40.2788,18.3436),
    Citta('Santarcangelo di Romagna','Emilia Romagna','RM',44.0617,12.4442),
    Citta('Stresa','Piemonte','VCO',45.8892,8.5368),
    Citta('Ladispoli','Lazio','RM',41.9506,12.0575),
    Citta('Palau','Sardegna','OT',41.1847,9.3816)
]
def salva_csv(file_nome,lista_citta):
    with open(file_nome,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(['nome','regione','provincia','lat','lon'])
        for c in lista_citta:
            writer.writerow([c.nome,c.regione,c.provincia,c.lat,c.lon])
def carica_csv(file_nome):
    lista=[]
    with open(file_nome,'r')as file:
        reader=csv.reader(file)
        next(reader)
        for nome,regione,provincia,lat,lon in reader:
            lista.append(Citta(nome,regione,provincia,float(lat),float(lon)))
    return lista
def trova_citta(lista,nome):
    nome_lower=nome.lower().strip()
    for citta in lista:
        if citta.nome.lower()==nome_lower:
            return citta
    return None
def elenca_citta(lista):
    print('\n'+'='*70)
    print('Città disponibili')
    print('='*70)
    for i,citta in enumerate(lista,1):
        print(f'{i}. {citta.nome:35} - {citta.regione:20} ({citta.provincia})')
    print('='*70+'\n')

def calcola_distanza_interattiva(lista):
    elenca_citta(lista)
    while True:
        print('\nInserisci il nome della prima citta (o "indietro" per tornare al menù):')
        citta1_nome=input('>').strip()
        if citta1_nome.lower()=='indietro':
            return
        citta1=trova_citta(lista,citta1_nome)
        if not citta1:
            print(f'Citta {citta1_nome} non trovato.Riprova')
            continue
        print(f'\n✓ Selezionata: {citta1.nome} ({citta1.regione}, {citta1.provincia})')

        print(f'\nInserisci il nome della seconda città')
        citta2_nome=input('>').strip()
        citta2=trova_citta(lista,citta2_nome)
        if not citta2:
            print(f'\nCittà "{citta2_nome}" non trovata.Riprova')
            continue
        print(f'\n✓ Selezionata "{citta2_nome}" ({citta2.regione}, {citta2.provincia})' )

        distanza=citta1.distanza(citta2)
        print(f'\n'+'='*60)
        print(f'Distanza tra {citta1.nome} e {citta2.nome}:')
        print(f'{distanza} KM')
        print('='*60 +'\n')
        continua=input("Vuoi calcolare un'altra distanza?(s/n):").strip().lower()
        if continua!='s':
            return
def calcola_tutte_distanze(lista):
    print(f'\n'+'='*60)
    print(f'DISTANZE TRA TUTTI I COMUNI')
    print('='*60 +'\n')
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            a1,a2=lista[i],lista[j]
            dist=a1.distanza(a2)
            print(f'{a1.nome:20} - {a2.nome:20}: {dist:6.2f} KM')
    print()
def crea_mappa(lista,file_mappa='mappa_colorata.html'):
    m=folium.Map(location=[43,12],zoom_start=6)
    for c in lista:
        folium.Marker([c.lat,c.lon], popup=f"<b>{c.nome}</b><br>{c.regione}<br>{c.provincia}").add_to(m)
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            c1,c2=lista[i],lista[j]
            dist= c1.distanza(c2)
            if dist<200:
                folium.PolyLine(
                    [(c1.lat,c1.lon),(c2.lat,c2.lon)],
                    color='brown',
                    popup=f'{dist} KM'
                ).add_to(m) 
                mid_lat=(c1.lat+c2.lat)/2
                mid_lon=(c1.lon+c2.lon)/2 
                folium.Marker(
                    [mid_lat,mid_lon],
                    icon=folium.DivIcon(
                        html=f"<div style='font-size:10pt;color:black;'>{dist}km</div>"
                    )
                ).add_to(m)
    m.save(file_mappa)
    print(f' Mappa salvata in {file_mappa}')

def menu_principale(lista):
    while True:
        print("\n" + "="*60)
        print("MANAGER CITTA' ITALIANE")
        print("="*60)
        print("1. Calcola distanza tra due città")
        print("2. Visualizza tutte le distanze")
        print("3. Elenca tutte le città")
        print("4. Crea mappa interattiva")
        print("5. Esci")
        print("="*60)

        scelta=input(f"\nScegli un'opzione (1-5)").strip()
        if scelta=='1':
            calcola_distanza_interattiva(lista)
        elif scelta=='2':
            calcola_tutte_distanze(lista)
        elif scelta=='3':
            elenca_citta(lista)
        elif scelta=='4':
            crea_mappa(lista)
            apri=input('Aprire la mappa nel browser? (s/n):').strip().lower()
            if apri=='s':
                webbrowser.open(os.path.abspath('mappa_colorata.html'))
        elif scelta=='5':
            print('Arrivederci')
            break
    else:
        print('Opzione non valida, riprova!')
if __name__=='__main__':
    salva_csv('citta.csv', lista_citta)
    citta_caricate=carica_csv('citta.csv')
    menu_principale(citta_caricate)







