#Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari.

numero = int(input("Inserisci un numero. Ti dico se è pari o dispari: "))

if numero%2 == 0:
    print(f"Il {numero} è pari")

else:
    print(f"Il numero {numero} è dispari")
