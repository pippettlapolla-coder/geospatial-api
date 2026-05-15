import csv
class Inventario:
    def __init__(self):
        self.oggetti=[]
    def aggiungi_oggetto(self,nome,quantita):
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
            print('Oggetto non trovato')

                

    def mostra(self):
        for nome,quantita in self.oggetti:
            print(f'{nome} : {quantita}')
    def salva_csv(self,file_nome):
        with open(file_nome, 'w', newline='')as file:
            writer=csv.writer(file)
            for oggetto in self.oggetti:
                writer.writerow(oggetto)

inventario = Inventario()

inventario.aggiungi_oggetto("Spada",1)
inventario.aggiungi_oggetto("Pozione",3)
inventario.aggiungi_oggetto("Scudo",1)
inventario.rimuovi_oggetto('Pozione',1)

inventario.mostra()

inventario.salva_csv("inventario.csv")

        