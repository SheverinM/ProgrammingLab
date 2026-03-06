#Scrivere un programma che chiede all’utente un numero intero e 
#stampa il suo quadrato e il suo cubo

def quadrato (n):
    
    return n**2

def cubo (n):
    
    return n**3


numero = int(input("inserisci un numero intero e ti restituisco"
                   " il suo quadrato e il suo cubo:"))


print(f"Il quadrato del numero \"{numero}\" è {quadrato(numero)}")
      
print(f"Il quadrato del numero \"{numero}\" è {cubo(numero)}") 


