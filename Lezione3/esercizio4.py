"""Scrivere una funzione che prended in input due liste e 
ritorna True se le due liste hanno almeno un elemento in comune e numero di elementi in comune."""

def Liste_elementi_in_comune(A, B):
    
    """
    
        Args: 
                A, B: liste 
    
        Variables:

                in_comune = numero di elementi in comune
                presente = un valore booleano --> se esistono elementi in comune = True altrimenti = False
        
        Returns: 
        
                True se almeno uun elento in comune, False altrimenti
                int: in_comune
    """

    in_comune = 0
    
    for i in A:
        for j in B:
            if i == j:
                in_comune +=1

    presente = in_comune > 0 
    
    return presente, in_comune


l
    