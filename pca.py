#implementação do método proposto (pca). À princípio, uso o Dataset
#Banknote Authentication. Faço a comparação de desempenho com o K-NN
#usando 1, 3, 5 vizinhos.

import math
from k_nn import *

#Operações com o arquivo contendo a database
with open('data_banknote_authentication.txt','r') as f:
    data = f.read()
    for char in [',']:
        if char in data:
            data = data.replace(char, '\n')

with open('data_banknote_authentication_final.txt', 'w') as f2:
    f2.write(data)

with open('data_banknote_authentication_final.txt', 'r') as f2:
    conteudo = f2.readlines()


#Função para dividir corretamente as informações da database em uma matriz de listas contendo os exemplos
def dividir(lista, n):
    for i in range (0, len(conteudo), n):
        yield lista[i:i + n]

#divisão dos conjuntos de teste/treino
lista = list(dividir(conteudo, 5))
#print(lista[761])
conjunto_treino_classe0 = lista[0:228] #1 - 762 (0.3% da base. Foram separados os valores em sequência)
print(lista[762])
conjunto_treino_classe1 = lista[762:945] #763 - 1372 (0.3% da base. Foram separados os valores em sequência)
#conjuto de trino
conjunto_treino = conjunto_treino_classe0 + conjunto_treino_classe1
#definição do conjunto de teste
conjunto_teste = lista[229:761] + lista[946:1371]


#Implementação do método proposto (pca)
def pca(dataset):
    atributo0_classe0 = []
    atributo1_classe0 = []
    atributo2_classe0 = []
    atributo3_classe0 = []

    for obj in range(len(dataset)):
        atributo0_classe0.append(dataset[obj][0])
        #print(atributo0_classe0[obj])
        atributo1_classe0.append(dataset[obj][1])
        #print(atributo1_classe0[obj])
        atributo2_classe0.append(dataset[obj][2])
        #print(atributo2_classe0[obj])
        atributo3_classe0.append(dataset[obj][3])
        #print(atributo3_classe0[obj])
        
    x_linha = 1/len(dataset)
    somat = 0

    for cont in atributo0_classe0:
        somat += float(cont)
        #print(somat)

    x_linha = x_linha * somat
    #print(x_linha)

    matriz_X_linha = []
    
    for k in range(len(atributo0_classe0)):
        matriz_X_linha.append(float(atributo0_classe0[k]) -  x_linha)
        #print(matriz_X_linha[k])
    print(matriz_X_linha)

    
acertos = 0


#classificação do Dataset puro.
for item in conjunto_teste:
    classe = knn(conjunto_treino, item, 1)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(conjunto_treino, item, 3)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(conjunto_treino, item, 5)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos:",100*acertos/len(conjunto_teste))

pca(conjunto_treino_classe0)




    
