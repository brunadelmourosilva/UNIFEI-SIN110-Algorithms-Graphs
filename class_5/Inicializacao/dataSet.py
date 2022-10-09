'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

dataSet - Funções de leitura de um dataset, criação das estruturas de representação de grafos e salvamento de resultados em arquivo.

05/09/2022
===================================================='''

import numpy as np

'''Cria Matriz de Adjacência: Função para leitura de um dataset em forma de matriz de adjacências.
Entrada: instancia (nome do arquivo .txt do dataset em forma de matriz de adjacência
Saída: matriz de adjacência (tipo NumPy.ndarray)'''
def criaMatrizAdjacencias(instancia):
    print('NOME DA INSTÂNCIA:', instancia, '\n')
    caminho = '/home/bdelmouro/IdeaProjects/My Projects/UNIFEI/UNIFEI-SIN110-Algorithms-Graphs/class_5/Instancias/' + instancia + '.txt'
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64") #OBS. Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data

'''Salva Resultado: Função para salvar em arquivo .txt o resultado da execução do programa.
Entrada: resultado (tipo lista)
Saída: arquivo .txt no diretório especificado'''
def salvaResultado(resultado, funcao):
    stringRes = ''
    for res in resultado:
        stringRes += str(res) + ' '
    arquivo = open('/home/bdelmouro/IdeaProjects/My Projects/UNIFEI/UNIFEI-SIN110-Algorithms-Graphs/class_3/grafo/Resultados/Arquivos/{}.txt'.format(funcao), 'a+')
    arquivo.writelines(stringRes + '\n')
    arquivo.close()