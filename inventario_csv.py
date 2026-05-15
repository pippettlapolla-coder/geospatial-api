import csv
class Inventario:
    def __init__(self):
        self.oggetti=[]
    def aggiungi_oggetto(self,nome,quantita):
        for i, (nome_oggetto,q) in enumerate(self.oggetti):
            if nome_oggetto==nome:
                self.oggetti[i]=(nome,q+quantita) 
                return
        self.oggetti.append((nome,quantita))
    def rimuovi_oggetto(self,nome,quantita):
        for i, (nome_oggetto,q) in enumerate(self.oggetti):
            if nome_oggetto == nome:
                nuova_quantita=q-quantita
                if nuova_quantita>0:
                    self.oggetti[i]=(nome,nuova_quantita)
                else:
                    self.oggetti.pop(i)
                return
        print(f'Oggetto "{nome}" non trovato')
    def mostra(self):
        for nome,quantita in self.oggetti:
            print(f'{nome} : {quantita}')
    def salva_csv(self,file_nome):
        with open(file_nome, 'w', newline='')as file:
            writer=csv.writer(file)
            for oggetto in self.oggetti:
                writer.writerow(oggetto)
    def carica_csv(self,file_nome):
        with open(file_nome,'r')as file:
            reader=csv.reader(file)

            for riga in reader:
                nome=riga[0]
                quantita=int(riga[1])
                self.aggiungi_oggetto(nome,quantita)

    def cerca_oggetto(self,nome):
        for nome_oggetto,q in self.oggetti:
            if nome_oggetto == nome:
                return q
        return None
    def aggiorna_oggetto(self,nome,nuova_quantita):
        for i, (nome_oggetto,q) in enumerate (self.oggetti):
            if nome_oggetto==nome:
                self.oggetti[i]=(nome,nuova_quantita) 
                return
        print('Oggetto non trovato')



inventario = Inventario()

inventario.aggiungi_oggetto("Spada",1)
inventario.aggiungi_oggetto("Pozione",3)
inventario.aggiungi_oggetto("Scudo",1)

inventario.aggiungi_oggetto('Mela',50)
inv = Inventario()

inv.aggiungi_oggetto("Spada", 1)

print("Quantità pozioni:", inv.cerca_oggetto("Pozione"))

inv.aggiorna_oggetto("Pozione", 10)
print("Quantità pozioni aggiornata:", inv.cerca_oggetto("Pozione"))

inv.mostra()
inventario.mostra()

inventario.salva_csv("inventario.csv")

        