import os
def calcolatore(a,b,operazione):
    operazioni={
        '+':lambda:a+b,
        '-':lambda:a-b,
        '/':lambda:a/b,
        '*':lambda:a*b,
        '**':lambda:a**b
    }
    operazione=operazione.strip()
    if operazione in operazioni:
        return operazioni[operazione]()
    else:
        return 'Comando non valido'
percorso_file = "C:/Users/Lapol/OneDrive/Desktop/prove python/risultati.txt"
print(f"File salvato in: {os.path.abspath(percorso_file)}")       

risultati=[]
while True:
    try:
        a=float(input('Inserisci il primo numero: '))
    except ValueError:
        print('Devi inserire un numero!')
        continue
    try:
        b=float(input('Inserisci il secondo numero: '))
    except ValueError:
        print('Devi inserire un numero!')
        continue
    op=input('Operazione (+,-,/,*,** o digita "stop" per uscire): ')
    if op.lower().strip()=='stop':
        break
    elif op.strip()=='/' and b ==0:
        print('Non si può dividere per 0!')
        continue
   
    else:
        risultato=calcolatore(a,b,op)
        print('Risultato', risultato)
        if isinstance(risultato,(int,float)):
            risultati.append(risultato)
            with open(percorso_file,'a')as file:
                file.write(str(risultato) + '\n')
            print('La lista di tutti i risultati ottenuti:', risultati)


    

        




        
        
        
        

        


        

        
   


    


        
