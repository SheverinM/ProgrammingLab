#Definire una funzione che dati 3 numeri interi stabilisce se 
# possono essere i valori dei lati di un triangolo e, se sì, di che tipo di triangolo.

"""Verificare che sia davvero un triangolo:

        I tre lati devono soddisfare la disuguaglianza triangolare:

                    a+b>c a+c>b b+c>a"""
"""
Equilatero --> a=b=c

Isoscele --> due lati uguali: a=b oppure a=c oppure b=c

Scaleno --> tutti i lati diversi: a != b != c
"""

def verifica_lati_triangolo(a, b, c):

    """è la funzione che verifica che i numeri inseriti possono essere lati di
    un triangolo.
    a, b, c sono numeri interi inseriti dall'utente
    
    la verifica_lati_triangolo ritorna valore True se i lati possono fare un triangolo"""

    triangolo = False

    if a + b > c and a + c > b and b + c > a:

        triangolo = True
    
    return triangolo

"""
def tipo_triangolo(a, b, c):

    if a == b == c:

        return "Equilatero"
    
    elif a==b or a==c or b==c:

        return "Isoscele"
    
    else:

        return "Scaleno"
"""


a = int(input("Inserisci II° lato:"))
b = int(input("Inserisci I° lato:"))
c = int(input("Inserisci III° lato:"))

"""if verifica_lati_triangolo:

    print(f"sono lati di un tringolo {tipo_triangolo(a,b,c)}")
"""
    