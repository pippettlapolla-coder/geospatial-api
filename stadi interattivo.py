import math
import csv
import folium
import webbrowser
import os

class Stadio:
    def __init__(self, nome, squadra, citta, lat, lon):
        self.nome = nome
        self.squadra = squadra
        self.citta = citta
        self.lat = lat
        self.lon = lon

    def distanza(self, altro):
        R = 6371  # raggio terrestre in km
        lat1, lon1 = math.radians(self.lat), math.radians(self.lon)
        lat2, lon2 = math.radians(altro.lat), math.radians(altro.lon)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * c, 2)

    def info(self):
        print(f"{self.nome} stadio della squadra {self.squadra}, ubicato a {self.citta} ({self.lat}, {self.lon})")

# lista stadi
STADI = [
    Stadio('San_Siro', 'Milan/Inter', 'Milano', 45.4781, 9.1239),
    Stadio('Olimpico','Lazio/Roma','Roma', 41.9336, 12.4546),
    Stadio('Allianz','Juventus','Torino', 45.1094, 7.6411),
    Stadio('Artemio_Franchi','Fiorentina','Firenze', 43.8070, 11.2587),
    Stadio('Maradona','Napoli','Napoli', 40.8359, 14.2463),
    Stadio('Dall_Ara','Bologna','Bologna', 44.4950, 11.3390),
    Stadio('Ferraris','Genoa','Genova', 44.4962, 8.9333),
    Stadio('Friuli','Udinese','Udine', 46.0650, 13.2340),
    Stadio('Gewiss','Atalanta','Bergamo', 45.6895, 9.6773),
    Stadio('Curi','Perugia','Perugia', 43.0953, 12.5741),
    Stadio('San_Nicola','Bari','Bari', 41.0842, 16.8374)
]

def salva_csv(file_nome, lista_stadi):
    with open(file_nome, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'squadra', 'citta', 'lat', 'lon'])
        for s in lista_stadi:
            writer.writerow([s.nome, s.squadra, s.citta, s.lat, s.lon])

def carica_csv(file_nome):
    lista = []
    with open(file_nome, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for nome, squadra, citta, lat, lon in reader:
            lista.append(Stadio(nome, squadra, citta, float(lat), float(lon)))
    return lista

def trova_stadio(lista, nome):
    """Cerca uno stadio per nome (case-insensitive)"""
    nome_lower = nome.lower().strip()
    for stadio in lista:
        if stadio.nome.lower() == nome_lower:
            return stadio
    return None

def elenca_stadi(lista):
    """Mostra tutti gli stadi disponibili"""
    print("\n" + "="*60)
    print("STADI DISPONIBILI:")
    print("="*60)
    for i, stadio in enumerate(lista, 1):
        print(f"{i}. {stadio.nome:20} - {stadio.squadra:20} ({stadio.citta})")
    print("="*60 + "\n")

def calcola_distanza_interattiva(lista):
    """Calcola la distanza tra due stadi scelti dall'utente"""
    elenca_stadi(lista)
    
    while True:
        print("\nInserisci il nome del primo stadio (o 'indietro' per tornare al menu):")
        stadio1_nome = input("> ").strip()
        
        if stadio1_nome.lower() == 'indietro':
            return
        
        stadio1 = trova_stadio(lista, stadio1_nome)
        if not stadio1:
            print(f"❌ Stadio '{stadio1_nome}' non trovato. Riprova.")
            continue
        
        print(f"\n✓ Selezionato: {stadio1.nome} ({stadio1.squadra})")
        
        print("\nInserisci il nome del secondo stadio:")
        stadio2_nome = input("> ").strip()
        
        stadio2 = trova_stadio(lista, stadio2_nome)
        if not stadio2:
            print(f"❌ Stadio '{stadio2_nome}' non trovato. Riprova.")
            continue
        
        print(f"\n✓ Selezionato: {stadio2.nome} ({stadio2.squadra})")
        
        distanza = stadio1.distanza(stadio2)
        print("\n" + "="*60)
        print(f"DISTANZA TRA {stadio1.nome} E {stadio2.nome}:")
        print(f"📍 {distanza} KM")
        print("="*60 + "\n")
        
        continua = input("Vuoi calcolare un'altra distanza? (s/n): ").strip().lower()
        if continua != 's':
            return

def calcola_tutte_distanze(lista):
    """Calcola tutte le distanze tra gli stadi"""
    print("\n" + "="*60)
    print("DISTANZE TRA TUTTI GLI STADI:")
    print("="*60 + "\n")
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            a1, a2 = lista[i], lista[j]
            dist = a1.distanza(a2)
            print(f"{a1.nome:20} - {a2.nome:20}: {dist:6.2f} KM")
    print()

def crea_mappa(lista, file_mappa='mappa_stadi.html'):
    """Crea una mappa interattiva con i stadi"""
    m = folium.Map(location=[43, 12], zoom_start=6)
    
    for s in lista:
        folium.Marker([s.lat, s.lon], popup=f"<b>{s.nome}</b><br>{s.squadra}<br>{s.citta}").add_to(m)

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            s1, s2 = lista[i], lista[j]
            dist = s1.distanza(s2)
            if dist < 200:
                folium.PolyLine(
                    [(s1.lat, s1.lon), (s2.lat, s2.lon)],
                    color='blue',
                    popup=f"{dist} km"
                ).add_to(m)
                mid_lat = (s1.lat + s2.lat) / 2
                mid_lon = (s1.lon + s2.lon) / 2
                folium.Marker(
                    [mid_lat, mid_lon],
                    icon=folium.DivIcon(
                        html=f"<div style='font-size:10pt; color:black;'>{dist} km</div>"
                    )
                ).add_to(m)
    
    m.save(file_mappa)
    print(f"✓ Mappa salvata in {file_mappa}")

def menu_principale(lista):
    """Menu interattivo principale"""
    while True:
        print("\n" + "="*60)
        print("MANAGER STADI ITALIANI")
        print("="*60)
        print("1. Calcola distanza tra due stadi")
        print("2. Visualizza tutte le distanze")
        print("3. Elenca tutti gli stadi")
        print("4. Crea mappa interattiva")
        print("5. Esci")
        print("="*60)
        
        scelta = input("\nScegli un'opzione (1-5): ").strip()
        
        if scelta == '1':
            calcola_distanza_interattiva(lista)
        elif scelta == '2':
            calcola_tutte_distanze(lista)
        elif scelta == '3':
            elenca_stadi(lista)
        elif scelta == '4':
            crea_mappa(lista)
            apri = input("Aprire la mappa nel browser? (s/n): ").strip().lower()
            if apri == 's':
                webbrowser.open(os.path.abspath('mappa_stadi.html'))
        elif scelta == '5':
            print("Arrivederci! 👋")
            break
        else:
            print("❌ Opzione non valida. Riprova.")

# Esecuzione
if __name__ == "__main__":
    salva_csv('stadi.csv', STADI)
    stadi_caricati = carica_csv('stadi.csv')
    menu_principale(stadi_caricati)