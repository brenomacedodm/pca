#importacao txt

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
#print(lista[762])
conjunto_treino_classe1 = lista[762:945] #763 - 1372 (0.3% da base. Foram separados os valores em sequência)
#conjuto de trino
conjunto_treino = conjunto_treino_classe0 + conjunto_treino_classe1
#definição do conjunto de teste
conjunto_teste = lista[229:761] + lista[946:1371]

def conjuntoTeste():
    return conjunto_teste

def conjuntoTreino():
    return conjunto_treino

def classe0():
    return conjunto_treino_classe0

def classe1():
    return conjunto_treino_classe1
