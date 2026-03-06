#Definire una funzione che prende come argomento una parola e una lettera 
# e ritorna quante volte quella lettera è contenuta nella parola.

def conta_ripetizione_lettera(parola, lettera):

    contatore = 0

    parola = parola.lower()

    lettera = lettera.lower()

    for c in parola:
        if c == lettera:
            contatore += 1

    return contatore

print("Inserisci una parola e una lettera e ti dico quante volte quella lettera",
      "è contenuta nella parola. cominciamo:")

parola = input("Inserisci una parola:")

lettera = input("Inserisci una lettera:")

ripetizioni = conta_ripetizione_lettera(parola, lettera)

print(f"La lettera \"{lettera}\" è stata ripetuta {ripetizioni} volte nella parola \"{parola}\"")


