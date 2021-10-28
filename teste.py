import k_nn
import pca

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