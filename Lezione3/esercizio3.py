

def scambia_elementi_lista(A, i, j):
    """
        Definire una funzione che prende in input una lista A, indici i e j e scambia il valore di A[i] con A[j]

        Args: A: lista.
                   i, j: due indici della lista A
        
        """

    elemento_i_esimo = A[i]
    elemento_j_esimo = A[j]
 
    A[i] = elemento_j_esimo
    A[j] = elemento_i_esimo


lista = ["Maria", "Majid", "Zagros", "Trilli"]

scambia_elementi_lista(lista, 0, 3)

print(lista)
