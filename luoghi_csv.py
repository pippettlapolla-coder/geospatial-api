import csv
import math


# Funzione esterna alla classe
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
    def aggiungi_luogo(self,luogo,lat,lon):
        for nome,_,_ in self.luoghi:
            if nome==luogo:
                print('Luogo già presente')
                return
        self.luoghi.append((luogo,lat,lon))
    def mostra_luogo(self):
        for nome,lat,lon in self.luoghi:
            print(f'{nome} : {lat}, {lon}')
    def rimuovi_luogo(self,luogo):
        for i,(nome,lat,lon) in enumerate(self.luoghi):
            if nome==luogo:
                self.luoghi.pop(i)
                return
        print('Luogo non trovato')
    def calcola_distanza(self,luogo1,luogo2):
        coord={nome:(lat,lon)for nome,lat,lon in self.luoghi}
        if luogo1 not in coord or luogo2 not in coord:
            print('Uno dei due luoghi, o entrambi, non esiste/esistono')
            return None
        lat1,lon1=coord[luogo1]
        lat2,lon2=coord[luogo2]
        return distanza_haversine(lat1,lon1,lat2,lon2)
    def salva_csv(self,file_nome):
        with open(file_nome,'w',newline='')as file:
            writer=csv.writer(file)
            for luogo in self.luoghi:
                writer.writerow(luogo)
        
    def carica_csv(self,file_nome): 
        with open(file_nome,'r')as file:
            reader=csv.reader(file)  
            self.luoghi=[]     
            for riga in reader:
                luogo=riga[0]
                lat=float(riga[1])
                lon=float(riga[2])
                self.luoghi.append((luogo,lat,lon))



luoghi = Luoghi()

luoghi.aggiungi_luogo("Roma",41.9,12.4)
luoghi.aggiungi_luogo("Milano",45.4,9.1)

luoghi.salva_csv("citta.csv")

luoghi.carica_csv("citta.csv")

luoghi.mostra_luogo()
d = luoghi.calcola_distanza("Roma", "Milano")
print(f"Distanza Roma-Milano: {d:.2f} km")
