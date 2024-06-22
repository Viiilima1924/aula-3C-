import statistics

ensino_fundamental1= [1,8,9,10,3,5,8,8,9]

def moda():
    ensino_fundamental = [1,8,9,10,3,5,8,8,9]
    moda1 =statistics.mode(ensino_fundamental1)
    print("Moda ensino fundamental - ", moda1)
    

moda()

import statistics

ensino_medio = list(range(1,151))

def moda0():
    ensino_medio = list(range(1,151))
    moda2 =  statistics.mode(ensino_medio)
    print("Moda ensino médio - ", moda2)
    

moda0()