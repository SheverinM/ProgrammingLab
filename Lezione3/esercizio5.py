"""Definire una funzione che prende in input una lista di numeri interi in [0,9] e ritorna una lista di stringhe, 
corrispondenti ai numeri scritti in italiano. Ad esempio [1,0,7,9,8] --> ["uno","zero","sette","nove","otto"]"""

def corrispondeza_cifre_lettere(A):
    """
        Args:
                A = lista di numeri interi
        
        Return:

                s = Stringa corrispondente ai numeri interi di A
    """

    cifre_lettere = {0:"Zero",1:"Uno",2: "Due",3:"Tre",4:"Quattro",
                     5:"Cinque",6:"Sei",7:"Sette", 8:"Otto",9:"Nove"}
    
    in_lettere = []
    
    for i in A:
        if i in cifre_lettere:
            in_lettere.append(cifre_lettere[i])                      
                    
    return in_lettere


lista_numeri = [1,2,4,6,7,0]

print(corrispondeza_cifre_lettere(lista_numeri))