#implementação do método proposto (pca). À princípio, uso o Dataset
#Banknote Authentication. Faço a comparação de desempenho com o K-NN
#usando 1, 3, 5 vizinhos.

import math

#Implementação do método proposto (pca)
'''def pca(dataset):

    #criação dos vetores colunas
    atributo0_classe0 = []
    atributo1_classe0 = []
    atributo2_classe0 = []
    atributo3_classe0 = []

    for obj in range(len(dataset)):
        atributo0_classe0.append(dataset[a][0])
        #print(atributo0_classe0[obj])
        atributo1_classe0.append(dataset[a][1])
        #print(atributo1_classe0[obj])
        atributo2_classe0.append(dataset[a][2])
        #print(atributo2_classe0[obj])
        atributo3_classe0.append(dataset[a][3])
        #print(atributo3_classe0[obj])
        
    x_linha = 1/len(dataset)
    x_linha2 = 1/len(dataset)
    x_linha3 = 1/len(dataset)
    x_linha4 = 1/len(dataset)
    somat = 0
    somat2 = 0
    somat3 = 0
    somat4 = 0

    for cont in range(len(dataset)):
        somat += float(atributo0_classe0[cont])
        somat2 = float(atributo1_classe0[cont])
        somat3 = float(atributo2_classe0[cont])
        somat4 = float(atributo3_classe0[cont])
        #print(somat)

    x_linha = x_linha * somat
    x_linha2 = x_linha2 * somat
    x_linha3 = x_linha3 * somat
    x_linha4 = x_linha4 * somat
    
    #print(x_linha)

    matriz_centrada_atr0 = []
    matriz_centrada_atr1 = []
    matriz_centrada_atr2 = []
    matriz_centrada_atr3 = []
    
    for k in range(len(dataset)):
        matriz_centrada_atr0.append(float(atributo0_classe0[k]) -  x_linha)
        matriz_centrada_atr1.append(float(atributo1_classe0[k]) -  x_linha)
        matriz_centrada_atr2.append(float(atributo2_classe0[k]) -  x_linha)
        matriz_centrada_atr3.append(float(atributo3_classe0[k]) -  x_linha)
        #print(matriz_X_linha[k])
    print(matriz_centrada_atr0)
    print(matriz_centrada_atr1)
    print(matriz_centrada_atr2)
    print(matriz_centrada_atr3)

    
acertos = 0


#classificação do Dataset puro.
#for item in conjunto_teste:
 #   classe = knn(conjunto_treino, item, 1)
  #  if item[4] == classe:
   #     acertos += 1

#print("Porcentagem de acertos:",100*acertos/len(conjunto_teste))

#acertos = 0

#for item in conjunto_teste:
#    classe = knn(conjunto_treino, item, 3)
#    if item[4] == classe:
#        acertos += 1

#print("Porcentagem de acertos:",100*acertos/len(conjunto_teste))

#acertos = 0

#for item in conjunto_teste:
#    classe = knn(conjunto_treino, item, 5)
#    if item[4] == classe:
#        acertos += 1

#print("Porcentagem de acertos:",100*acertos/len(conjunto_teste))

#pca(conjunto_treino_classe0)'''

def pca(dataset, qntd_atributos):

    #separação dos atributos
    atributo0 = []
    atributo1 = []
    atributo2 = []
    atributo3 = []

    for obj in range(len(dataset)):
        atributo0.append(dataset[obj][0])
        #print(atributo0[obj])
        atributo1.append(dataset[obj][1])
        #print(atributo1[obj])
        atributo2.append(dataset[obj][2])
        #print(atributo2[obj])
        atributo3.append(dataset[obj][3])
        #print(atributo3[obj]


    #calculo das medias aritmeticas
    media0 = 0
    media1 = 0
    media2 = 0
    media3 = 0

    for k in range(len(dataset)):
        media0 += float(atributo0[k])
        media1 += float(atributo1[k])
        media2 += float(atributo2[k])
        media3 += float(atributo3[k])
    
    media0 /= len(atributo0)
    media1 /= len(atributo1)
    media2 /= len(atributo2)
    media3 /= len(atributo3)


    #calculo das variancias
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0

    for k in range(len(dataset)):
        var0 += pow(float((dataset[k][0]))-(media0),2)
        var1 += pow(float((dataset[k][1]))-(media1),2)
        var2 += pow(float((dataset[k][2]))-(media2),2)
        var3 += pow(float((dataset[k][3]))-(media3),2)

    var0 = math.sqrt(var0)
    var1 = math.sqrt(var1)
    var2 = math.sqrt(var2)
    var3 = math.sqrt(var3)
    
    vetor_var = [var0, var1, var2, var3]
    vetor_var.sort(reverse=True)

    m0, m1, m2, m3 = 0, 0, 0, 0
    
    if vetor_var[0] == var0:
        m0 = 0
        vetor_var.remove(var0)
    elif vetor_var[0] == var1:
        m0 = 1
        vetor_var.remove(var1)
    elif vetor_var[0] == var2:
        m0 = 2
        vetor_var.remove(var2)
    else:
        m0 = 3
        vetor_var.remove(var3)

    if vetor_var[0] == var0:
        m1 = 0
        vetor_var.remove(var0)
    elif vetor_var[0] == var1:
        m1 = 1
        vetor_var.remove(var1)
    elif vetor_var[0] == var2:
        m1 = 2
        vetor_var.remove(var2)
    else:
        m1 = 3
        vetor_var.remove(var3)

    if vetor_var[0] == var0:
        m2 = 0
        vetor_var.remove(var0)
    elif vetor_var[0] == var1:
        m2 = 1
        vetor_var.remove(var1)
    elif vetor_var[0] == var2:
        m2 = 2
        vetor_var.remove(var2)
    else:
        m2 = 3
        vetor_var.remove(var3)

    if vetor_var[0] == var0:
        m3 = 0
        vetor_var.remove(var0)
    elif vetor_var[0] == var1:
        m3 = 1
        vetor_var.remove(var1)
    elif vetor_var[0] == var2:
        m3 = 2
        vetor_var.remove(var2)
    else:
        m3 = 3
        vetor_var.remove(var3)
    

    #novo conjunto de treino usando o atributo com maior variancia
    atributo = []
    if qntd_atributos == 1:
        for k in range(len(dataset)):
            teste = [dataset[k][m0], dataset[k][m1], dataset[k][4]]
            atributo.append(teste)  
    elif qntd_atributos == 2:
        for k in range(len(dataset)):
            teste = [dataset[k][m0], dataset[k][m1], dataset[k][4]]
            atributo.append(teste)
    elif qntd_atributos == 3:
        for k in range(len(dataset)):
            teste = [dataset[k][m0], dataset[k][m1], dataset[k][m2], dataset[k][4]]
            atributo.append(teste)
    else:
        atributo = dataset
    
    return atributo


















    
