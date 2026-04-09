"""
    Scrivere una funzione che prende in input una stringa e ritorna True se è un
    palindromo, False altrimenti

    Args:
            parola: stringa

    Returns:

            verificato: True or False
    """

def palindroma(parola):

    """Adesso voglio escludere caratteri speciali dalla stringa ricevuta in modo da ottenere una
    stinga fatta soltanto dai caratteri dell'alfabeto:"""

    caratteri_da_escludere = [" ","!", "?", ".", ";", ":", "-", "_", "(", ")","'"]
    parola_senza_caratteri_speciali = "" #Devi creare la stinga vuota

    #mi creao la strimnga senza caratteri speciali, cioè una stringa di soli caratteri alfabetici
    for carattere in parola:
        if carattere not in caratteri_da_escludere:
            parola_senza_caratteri_speciali += carattere
                       
    
    """Adesso inverto la stinga che non ha caratteri speciali:"""

    parola_invertita = parola_senza_caratteri_speciali[::-1]        
  
    """ritrno un valore vero se le due stringhe sono uguali e un valore falso se sono diverse:"""
    
    return parola_invertita == parola_senza_caratteri_speciali


parola = "     Ai lati d'Italia!!  "

print(palindroma(parola))
