'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

08/10/2022
===================================================='''
import numpy as np


'''Tipo do grafo: Retorna o tipo do grafo representado por uma dada matriz de adjacências.
Entrada: matriz de adjacências
Saída: Integer (0 – simples; 1 – dígrafo; 2 – multigrafo; 3 – pseudografo)
'''
def tipoGrafo(matriz):
    diagonalEhZerada = True
    numerosLimitadosAZeroOuUm = True
    matrizAssimetrica = True

    qtdVertices = np.shape(matriz)[0]
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(vi + 1, qtdVertices):  # Para cada vértice vj
            if vi == vj:
                if matriz[vi][vj] != 0: #caso a diagonal possua valores diferentes de 0
                    diagonalEhZerada = False

            if matriz[vi][vj] > 1: #caso a matriz possua valores maiores que 1
                numerosLimitadosAZeroOuUm = False

            if matriz[vi][vj] == matriz[vj][vi]: #caso onde a posição dada e sua inversa sejam iguais
                matrizAssimetrica = False

    if diagonalEhZerada and numerosLimitadosAZeroOuUm: #grafo do tipo simples
        return 0
    elif matrizAssimetrica: #grafo do tipo dígrafo
        return 1
    elif diagonalEhZerada and not numerosLimitadosAZeroOuUm: #grafo do tipo multigrafo
        return 2
    elif not diagonalEhZerada and not numerosLimitadosAZeroOuUm: #grafo do tipo pseudrografo
        return 3

'''
Descrição: Obtém a matriz de alcançabilidade de um grafo com base no algoritmo de Warshall.
Entrada: matriz de adjacências (tipo numpy.ndarray)
Saída: matriz de acessibilidade (tipo numpy.ndarray)
'''
def warshall(matriz):
    qtdVertices = np.shape(matriz)[0]

    for k in range(0, qtdVertices):
        for i in range(0, qtdVertices):
            for j in range(0, qtdVertices):
                if matriz[i][j] == 1 or (matriz[i][k] == 1 and matriz[k][j] == 1):
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = matriz[i][j]

    print(matriz)
    return matriz

'''
Descrição: Verifica se um grafo possui um caminho Euleriano.
Entrada: matriz de adjacências (tipo numpy.ndarray)
Saída: True se grafo possui caminho Euleriano, False caso contrário (Boolean)
'''


def retornaGrauVertice(qtdVertices, vertice):
    pass


def caminhoEuleriano(matriz):
    qtdVertices = np.shape(matriz)[0]
    total = 0
    aux = 0

    #encontra o caminho euleriano
    while (total <= 2) and (aux <= qtdVertices):
        #retorna o grau do vértice na posição i
        for vertice in range(0, qtdVertices):
            degree = 0
            for vi in range(0, qtdVertices):
                if matriz[vertice][vi] == 1:
                    degree += 1

            # for vx in range(0, qtdVertices):
            if matriz[vertice][vertice] == 1:
                degree += 1

            if degree % 2 == 0:
                pass
            else:
                total += 1
                aux += 1

    if total > 2:
        print('False')
        return False
    else:
        print('True')
        return True


