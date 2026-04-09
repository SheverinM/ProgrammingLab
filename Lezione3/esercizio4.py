"""Scrivere una funzione che prended in input due liste e 
ritorna True se le due liste hanno almeno un elemento in comune."""

def Liste_elementi_in_comune(A, B):
    
    """
    Verifica la presenza di elementi comuni tra due liste.

    Args:
        A (list): La prima lista di elementi.
        B (list): La seconda lista di elementi.

    Return:
        bool: True se esiste almeno un elemento in comune, False altrimenti.
    """

    in_comune = 0
    
    for i in A:
        for j in B:
            if i == j:
                return True


lista1 = ["Majid", 1, 90, 4.5, "Zagros"]
lista2 = [10, "Majid", 30, [1,2,3], 90, 4.5]

print(Liste_elementi_in_comune(lista1,lista2))
