import numpy as np
import json
rubrica=dict()
def normalizza_nome(nome):
    return nome.lower().strip()
def aggiungi_contatto(nome, numero):
    chiave=normalizza_nome(nome)
    rubrica[chiave]={'nome':nome,'numero':numero}
def cerca_contatto(nome):
    chiave=normalizza_nome(nome)
    return rubrica.get(chiave)
def elimina_contatto(nome):
    chiave=normalizza_nome(nome)
    return rubrica.pop(chiave,None)
def mostra_rubrica():
    return rubrica
def carica_da_file():
    try:
        with open('rubrica.json','r')as file:
           return json.load(file)
    except FileNotFoundError:
        return {}
def salva_su_file(rubrica):
    with open('rubrica.json','w')as file:
        json.dump(rubrica,file)

carica_da_file()
while True:
    print("\n1. Aggiungi contatto")
    print("2. Cerca contatto")
    print("3. Elimina contatto")
    print("4. Mostra rubrica")
    print("5. Esci")

    scelta=input('Scegli: ')

    if scelta=='1':
        nome=input('Nome: ')
        numero=input('Numero: ')
        aggiungi_contatto(nome,numero)
        salva_su_file()
        print('Contatto salvato!')
    elif scelta=='2':
        nome=input('Nome da cercare: ')
        contatto=cerca_contatto(nome)
        if contatto:
            print(contatto['nome'],contatto['numero'])
        else:
            print('Non trovato!')
    elif scelta=='3':
        nome=input('Nome da eliminare: ')
        if elimina_contatto(nome):
            salva_su_file()
            print('Eliminato')
        else:
            print('Non trovato!')
    elif scelta=='4':
        for c in mostra_rubrica().values():
            print(c['nome'],'-',c['numero'])
    elif scelta=='5':
        print('Uscita...')
        break
    else:
        print('Opzione non valida')
        continue
    