import statistics

ensino_fundamental = [1,8,9,10,3,5,8,8,9]

def mediana():
    ensino_fundamental = [1,8,9,10,3,5,8,8,9]
    mediana1 = statistics.median(ensino_fundamental)
    print("Mediana ensino fundamental - " ,mediana1)

mediana()  

import statistics

ensino_medio = list(range(1,151))

def mediana2():
    ensino_medio = list(range(1,151))
    mediana12 =  statistics.mode(ensino_medio)
    print("Mediana ensino médio - ", mediana12)
    
mediana2()