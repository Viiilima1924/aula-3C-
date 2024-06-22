import statistics

ensino_fundamental = [1,8,9,10,3,5,8,8,9]

def media():
    ensino_fundamental = [1,8,9,10,3,5,8,8,9]
    media1 =  statistics.mean(ensino_fundamental)
    print("Média ensinofundamental1 - ", media1)
    

media()


ensino_medio = list(range(1,151))

def media1():
    ensino_medio = list(range(1,151))
    mediaalu =  statistics.mean(ensino_medio)
    print("Média ensino médio - ", mediaalu)
    

media1()