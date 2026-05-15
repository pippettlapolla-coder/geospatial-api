import csv
import math

# Funzione per calcolare distanza tra due punti (Haversine)
def distanza_haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c
class Luoghi:
    def __init__(self):
        self.luoghi=[]
    def aggiungi_luogo(self,nome,lat,lon):
        for l in self.luoghi:
            if l ['nome']==nome:
                print(f'{nome} già presente!')
                return
        self.luoghi.append({'nome':nome, 'lat':lat,'lon':lon})
    def mostra_luogo(self):
        for l in self.luoghi:
            print(f'{l['nome']} : {l['lat']}, {l['lon']}')
    def luoghi_vicini(self,lat,lon,raggio_km):
        vicini=[]
        for l in self.luoghi:
            d=distanza_haversine(lat,lon,l['lat'],l['lon'])
            if d<=raggio_km:
                vicini.append((l['nome'],d))
        return vicini
    def salva_csv(self,file_nome):
        with open(file_nome,'w', newline='')as file:
            writer=csv.writer(file)
            for l in self.luoghi:
                writer.writerow([l['nome'],l['lat'],l['lon']])
    def carica_csv(self,file_nome):
        self.luoghi=[]
        with open(file_nome,'r')as file:
            reader=csv.reader(file)
            for riga in reader:
                self.aggiungi_luogo(riga[0], float(riga[1]), float(riga[2]))
mappa=Luoghi()
mappa.aggiungi_luogo('Roma', 41.9,12.5)
mappa.aggiungi_luogo('Milano', 45.5,9.2)
mappa.aggiungi_luogo('Napoli', 40.8,14.2)
mappa.mostra_luogo()
vicini_a_roma=mappa.luoghi_vicini(41.9,12.5,400)
print(f' Luoghi entro 400 km da Roma:')
for nome, d in vicini_a_roma:
    print(f' {nome} a {d:.2f} km')