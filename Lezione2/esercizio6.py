# Scrivere un programma che fa la somma di n numeri inseriti dall’utente. 
# Di all'utente di scrivere 0 per fermarsi.

print("Inserisci n numeri e io ti faccio la somma di questi numeri.",
      "Inserisci 0 per fermarti.", sep="\n")

i = 1  # conta il numero dei numeri inseriti

numero = int(input(f"Inserisci {i}° numero: "))

somma = 0

while numero != 0:

    i += 1

    somma += numero

    numero = int(input(f"Inserisci {i}° numero:"))

    

print(f"la somma di {i} numeri che hai inserito è {somma}")