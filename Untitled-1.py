import random
class Arma:
    def __init__(self,arma,bonus_danno):
        self.nome=arma
        self.bonus_danno=bonus_danno
    def mostra(self):
        print(f'{self.nome}: (+{self.bonus_danno} danni)')
class Giocatore:
    def __init__(self,nome,arma):
        self.nome=nome
        self.vita=100
        self.arma=arma
        self.pozioni=2 

        self.livello=1
        self.xp=0
        self.xp_levelup=50
    def attacca(self):
        dado=random.randint(1,10)
        danno=random.randint(5,20)+ self.arma.bonus_danno
        if dado==1:
            print(f'{self.nome} manca il colpo')
            return 0
        elif dado==10:
            print(f'{self.nome} sferra un colpo critico!')
            return danno*2
        else:
            return danno
    def guadagna_punti(self,punti):
        self.xp+=punti
        print(f'{giocatore.nome} guadagna {punti}, {self.xp} XP totali.')
        while self.xp>=self.xp_levelup:
            self.xp-=self.xp_levelup
            self.livello+=1
            print(f'{giocatore.nome} sale al livello {self.livello}!')
            self.vita+=20
            self.pozioni+=1
            self.xp_levelup=int(self.xp_levelup *1.5)
    def subisci(self,danno):
        self.vita-=danno
        if self.vita<=0:
            print(f'{self.nome} sei morto')
    def cura(self):
        if self.pozioni>=1:
            self.vita=min(self.vita + 20,100)
            self.pozioni-=1
            print(f'{self.nome} usa Pozione e recupero 20 HP')
        else:
            print(f'{self.nome} ha terminato le pozioni')
    def mostra(self):
        print(f'{self.nome} : {self.vita} HP| Pozioni: {self.pozioni} | Livello: {self.livello}') 
class Mostro:
    def __init__(self,nome,vita,danno_min,danno_max,xp_dato):
        self.nome=nome
        self.vita=vita
        self.danno_min=danno_min
        self.danno_max=danno_max
        self.xp_dato=xp_dato
    def attacca(self):
        return random.randint(self.danno_min, self.danno_max)
    def subisci(self,danno):
        self.vita-=danno
        if self.vita<=0:
            self.vita=0
            print(f'{self.nome} è morto')
    def mostra(self):
        print(f'{self.nome} : {self.vita} HP') 
spada=Arma('Spada', 5)
giocatore=Giocatore('Ben', spada)
mostri=[
    Mostro('goblin', 50, 3,9,20),
    Mostro('Orco', 70,5,12,35),
    Mostro('Troll', 100,7,17,50)
]
for mostro in mostri:
    print(f'Un {mostro.nome} appare!')
    while giocatore.vita>0 and mostro.vita>0:
        print(f' Cosa vuoi fare?')
        print('1 Attacca')
        print('2 Usa pozione')
        print('3 Mostra stato')
        scelta=input('Scelta: ').strip()
        if scelta=='1':
            danno=giocatore.attacca()
            print(f'{giocatore.nome} attacca e infligge {danno} danni!')
            mostro.subisci(danno)
        elif scelta=='2':
            giocatore.cura()
        elif scelta=='3':
            giocatore.mostra()
            mostro.mostra()
            continue
        else:
            print('Scelta non valida!')
            continue
            
       
        if mostro.vita>0:
            danno_m=mostro.attacca()
            print(f'{mostro.nome} attacca e fa {danno_m} danni')
            giocatore.subisci(danno_m)

        giocatore.mostra()
        mostro.mostra()
    if giocatore.vita>0:
        print(f'{giocatore.nome} ha sconfitto {mostro.nome}!')
        giocatore.guadagna_punti(mostro.xp_dato)
    else:
        print(f'{mostro.nome} ha sconfitto {giocatore.nome}, il male ha vinto!')
        break
        
if giocatore.vita>0:
    print('Congratulazioni, hai sconfitto tutti i mostri, il mondo è salvo!')



        

    