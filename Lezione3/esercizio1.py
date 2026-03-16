"""
    somma degli elementi di una lista

    Args: 
            
            lista
    
    variables:

            somma = contiene somma dei elementi della lista
    
    Return:
            
            int or float: somma 
"""

def somma_elementi_lista(lista):
    somma = 0
    for i in lista:
        somma += lista[i]

    return somma