#Scrivere un programma che verifica se un numero inserito dall’utente è primo.

def numero_primo (n):

    """La funzione numero_primo ritorna True se numero inserito è primo e False se 
    numero inserito non è primo.
    
    n è un numero intero positivo e n > 1"""

    primo = True

    for i in range (2, n):

        if(n % i == 0):

            primo = False
        
    return primo


numero = int(input("Inserisci un numero e ti dico se è un numero primo: "))


if numero_primo (numero):

    print(f"Il numero \"{numero}\" è un numero primo")

else:
    
    print(f"Il numero \"{numero}\" non è un numero primo")