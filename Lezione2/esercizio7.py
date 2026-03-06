#Definire la funzione fattoriale (versione iterativa).

def fattoriale (n):

    fatt = 1

    for i in range(n):
            
            fatt *= i + 1
    
    return fatt

numero = int(input("inserisce un numero e te ne calcolo il fattoriale: "))

print(f"{numero}! = {fattoriale(numero)}")
    
