persona={
    'nome':'Luca',
    'cognome':'Rossi',
    'eta':25,  
}
operazioni=('aggiungere','modificare','eliminare')
def start():
    operazione=input('Cosa vuoi fare?: ')
    if operazione.strip()==operazioni[0]:
        x=input('Aggiungi una chiave:valore separati da una virgola: ')
        aggiungi(x.split(','))
    elif operazione==operazioni[1]:
        x = input('Modifica - Inserisci chiave:valore separati da una virgola: ')
        modifica(x.split(','))
    elif operazione==operazioni[2]:
        chiave = input('Elimina - Inserisci la chiave: ').strip()
        elimina(chiave)
def aggiungi(param):
    chiave=param[0]
    valore=param[1]
    persona[chiave]=valore
    print(persona)
def modifica(param):
    chiave=param[0].strip()
    valore=param[1].strip()
    if chiave in persona:
        persona[chiave]=valore
        print(f"✅ Modificato: {chiave} = {valore}")
        print(persona)
    else:
        print(f"❌ Errore: chiave '{chiave}' non esiste!")
def elimina(chiave):
    if chiave in persona:
        del persona[chiave]
        print(f"✅ Eliminato: {chiave}")
        print(persona)
    else:
        print(f"❌ Errore: chiave '{chiave}' non esiste!")

while True:
    start()
