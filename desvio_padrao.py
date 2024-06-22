import statistics 

ensino_fundamental = [1,8,9,10,3,5,8,8,9]

def desvio():
    ensino_fundamental = [1,8,9,10,3,5,8,8,9]
    desvio1 =  statistics.stdev(ensino_fundamental)
    print("Desvio ensino fundamental - " , desvio1)

desvio()

ensino_medio = list(range(1,151))

def desvio1():
    ensino_medio = list(range(1,151))
    desvio2 =  statistics.stdev(ensino_medio)
    print("Desvio ensino medio - " , desvio2)

desvio1()