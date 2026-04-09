#Definire una funzione che conta quante vocali sono presenti in una stringa.

def vocali_stringa(str):

    contatore = 0

    #vocale = ["a","e","i","o","u"]

    vocale = "aeiou"
    
    for lettera in str:
        if lettera.lower() in vocale:
            contatore += 1
    
    return contatore

print(vocali_stringa("CiAo MONDo"))