from k_nn import *
from pca import *
import ds_import

acertos = 0
conjunto_teste = []
conjunto_teste = ds_import.conjuntoTeste()
conjunto_treino = []
conjunto_treino = ds_import.conjuntoTreino()
treino0 =[]
treino0 = ds_import.classe0()
treino1 =[]
treino1 = ds_import.classe1()

#print(conjunto_treino[:2])

#classificação do Dataset puro.
for item in conjunto_teste:
    classe = knn(conjunto_treino, item, 1)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 1-nn:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(conjunto_treino, item, 3)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 3-nn:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(conjunto_treino, item, 5)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 5-nn:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(pca(conjunto_treino,1), item, 1)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 1-nn com 1 pca:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(pca(conjunto_treino,2), item, 1)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 1-nn com 2 pca:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(pca(conjunto_treino,3), item, 1)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 1-nn com 3 pca:",100*acertos/len(conjunto_teste))

acertos = 0

for item in conjunto_teste:
    classe = knn(pca(conjunto_treino,4), item, 1)
    if item[4] == classe:
        acertos += 1

print("Porcentagem de acertos 1-nn com 4 pca:",100*acertos/len(conjunto_teste))

