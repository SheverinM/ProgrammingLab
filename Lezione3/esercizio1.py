"""
Calcola la somma degli elementi di una lista.

Args:
    lista (list): Una lista di numeri (int o float).

Returns:
    int or float: La somma totale degli elementi.
"""

def somma_elementi_lista(lista):
    somma = 0
    for i in lista:
        somma += i

    return somma
    

lista_numeri = [1,2,3,4,5,6,7,8,9,10]
print(f"somma degli elementi della lista è {somma_elementi_lista(lista_numeri)}")


