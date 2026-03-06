#Definire una funzione che conta quante vocali sono presenti in una stringa.

def vocali_stringa (str):

    """La funzione vocali_stringa conta quante vocali sono presenti in una stringa
    str è la stinga """

    str_min = str.lower() 

    contatore = 0

    for i in str_min:

        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":

            contatore += 1
    
    return contatore


str_input = input("Inserisci una stringa e ti dico quante vocali contiene: ")

print(f"ci sono {vocali_stringa(str_input)} vocali in \"{str_input}\"")

