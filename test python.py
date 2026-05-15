import json
class Studente:
    def __init__(self,nome,eta):
        self.nome=nome
        self.eta=eta
        self.materie={}
    def __str__(self):
        return f'{self.nome} - {self.eta} anni '
    def aggiungi_materia(self,nome_materia):
        if nome_materia not in self.materie:
            self.materie[nome_materia]=Materia(nome_materia)
    def aggiungi_voto(self,materia,voto):
        if materia not in self.materie:
            self.aggiungi_materia(materia)
        self.materie[materia].aggiungi_voto(voto)
    def calcola_media(self):
        if len(self.materie)==0:
            return 0
        somma=sum(m.media()for m in self.materie.values())
        return somma/len(self.materie)   
    def media_generale(self):
        return self.calcola_media()
    def to_dict(self):
        return {
            'nome':self.nome,
            'eta':self.eta,
            'materie':{
                m: materia.voti
                for m, materia in self.materie.items()
            }
        }
    


def mostra_studenti(lista):
    for studente in lista:
        print(f'{studente.nome} ha una media di: {studente.calcola_media()}')
def media_maggiore(lista):
    media_max=-1
    migliore=None
    for studente in lista:
        media=studente.calcola_media()
        if media>media_max:
            media_max=media
            migliore=studente
    return migliore
class Materia:
    def __init__(self,nome):
        self.nome=nome
        self.voti=[]
    def aggiungi_voto(self,voto):
        self.voti.append(voto)
    def media(self):
        if len(self.voti)==0:
            return 0
        return sum(self.voti)/len(self.voti)
def salva_su_file(studente):
        with open('studente.json','w')as file:
            json.dump(studente.to_dict(),file,indent=4)
def carica_file():
    with open ('studente.json','r')as file:
        data=json.load(file)
    studente=Studente(data['nome'],data['eta'])    
    for nome_materia,voti in data['materie'].items():
        for voto in voti:
            studente.aggiungi_voto(nome_materia,voto)
    return studente

studenti=[]
s1=Studente('Luca',20)
studenti.append(s1)
s2=Studente('Marco',22)
studenti.append(s2)

studenti[0].aggiungi_voto('matematica',8)
studenti[0].aggiungi_voto('italiano',6)
studenti[1].aggiungi_voto('matematica',8)
studenti[1].aggiungi_voto('italiano',10)
salva_su_file(s2)
studenti.remove(s2)
s=carica_file()
m=media_maggiore(studenti)
print(m.nome,m.calcola_media())


