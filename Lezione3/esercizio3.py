
""" Definire una funzione che prende in input una lista A, indici i e j e scambia il valore di A[i] con A[j]"""

def scambia_elementi_lista(A, i, j):
    """
        Args: A: lista.
                   i, j: due indici della lista A
        
        """

    temp = A[i]
    A[i] = A[j]
    A[j] = temp

"""La soluzione Pythonica per fare questo scambio senza utilizzare varibile
temporale temp è:   A[i], A[j] = A[j], A[i]"""

lista = ["Maria", "Majid", "Zagros", "Trilli"]

scambia_elementi_lista(lista, 0, 3)

print(lista)
