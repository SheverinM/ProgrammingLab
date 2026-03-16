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
        somma += i

    return somma
    

lista_numeri = [1,2,3,4,5,6,7,8,9,10]
print(f"somma degli elementi della lista è {somma_elementi_lista(lista_numeri)}")


