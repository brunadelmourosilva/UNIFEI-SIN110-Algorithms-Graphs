'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

dataSet - Funções de leitura de um dataset, criação das estruturas de representação de grafos e salvamento de resultados em arquivo.

18/09/2022
===================================================='''

import numpy as np
from collections import defaultdict

'''Cria Matriz de Adjacência: Função para leitura de um dataset em forma de matriz de adjacências.
Entrada: instancia (nome do arquivo .txt do dataset em forma de matriz de adjacência
Saída: matriz de adjacência (tipo NumPy.ndarray)'''
def criaMatrizAdjacencias(instancia):
    print('NOME DA INSTÂNCIA:', instancia, '\n')
    caminho = '/home/bdelmouro/IdeaProjects/My Projects/UNIFEI/UNIFEI-SIN110-Algorithms-Graphs/class_4/grafo/Instancias/' + instancia + '.txt'
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64") #OBS. Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data

'''Cria Lista de Adjacência: Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências.
Entrada: matriz de adjacências (arquivo .txt)
Saída: lista de adjacências (tipo Dictionary)
'''
def criaListaAdjacencias(matriz):
    listaAdjacencia = defaultdict(list)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                listaAdjacencia[i].append(j)

    print("Lista de adjacência criada com sucesso!\n")

    #mostra lista de adjacência no console
    mostraListaAdjacencia(listaAdjacencia)

    #retorna o tipo 'dictionary'
    return listaAdjacencia

'''Mostrar lista de adjacência no console da aplicação
Entrada: lista de adjacências (tipo Dictionary)
Saída: lista de adjacência em print para o console
'''
def mostraListaAdjacencia(listaAdjacencia):
    for i in listaAdjacencia:
        print(i, end="")
        for j in listaAdjacencia[i]:
            print(" -> {}".format(j), end="")
        print()
    print()

'''Salva Resultado: Função para salvar em arquivo .txt o resultado da execução do programa.
Entrada: resultado (tipo lista)
Saída: arquivo .txt no diretório especificado'''
def salvaResultado(resultado, funcao):
    stringRes = ''
    for res in resultado:
        stringRes += str(res) + ' '
    arquivo = open('/home/bdelmouro/IdeaProjects/My Projects/UNIFEI/UNIFEI-SIN110-Algorithms-Graphs/class_4/grafo/Resultados/Arquivos/{}.txt'.format(funcao), 'a+')
    arquivo.writelines(stringRes + '\n')
    arquivo.close()