#Scrivere un programma che chiede all’utente un numero intero e 
#stampa il suo quadrato e il suo cubo

numero = int(input("inserisci un numero intero e ti restituisco"
                   "il suo quadrato e il suo cubo:"))

quadrato = numero**2
cubo = numero**3

print(f"Il quadrato del numreo {numero} = {quadrato}",
      f"Il cubo del numero {numero} = {cubo}", sep="\n")

