#função para cálculo da distância euclidiana

import math

def distancia_eucl(item_1, item_2):
    somatorio = 0
    for i in range(len(item_1)-1):
        somatorio += pow((float(item_1[i]) - float(item_2[i])),2)
    return math.sqrt(somatorio)


#Função do K-NN para comparar com o desempenho do método proposto
def knn (conjunto, item, k):
    distancias = []
    resultado = []
    nn = []
    
    for i in range(len(conjunto)):
        distancias.append(distancia_eucl(conjunto[i], item))
        
    resultado = sorted(distancias)[:k]

    qtdClasse0, qtdClasse1 = 0, 0
    
    for a in range(len(resultado)):
        if conjunto[distancias.index(resultado[a])][4] == "0\n":
            #print(conjunto[distancias.index(resultado[a])][4])
            qtdClasse0 += 1
        elif conjunto[distancias.index(resultado[a])][4] == "1\n":
            #print(conjunto[distancias.index(resultado[a])][4])
            qtdClasse1 += 1

    #print(qtdSet)
    #print(qtdVer)
    #print(qtdVir)
    
    if (qtdClasse0 > qtdClasse1):
        return "0\n"
    else:
        return "1\n"
