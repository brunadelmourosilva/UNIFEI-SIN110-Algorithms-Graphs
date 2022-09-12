'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''
import numpy
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


'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


'''Calcula densidade: Retorna o valor da densidade do grafo.
Entrada: matriz de adjacências
Saída: Float (valor da densidade com precisão de três casas decimais)
'''
def calcDensidade(self, matriz):
    # recebe o tipo do grafo para que a escolha do cálculo seja de acordo com o tipo retornado
    tipoGrafo = self.tipoGrafo(matriz)
    qtdVertices = np.shape(matriz)[0]

    if tipoGrafo == 0: #caso seja um grafo do tipo simples
        qtdArestas = 0
        for vi in range(0, qtdVertices):
            for vj in range(vi + 1, qtdVertices):
                if matriz[vi][vj] == 1: #se a posição for 1, significa que possui aresta
                    qtdArestas += 1 #realiza o calculo da quantidade de arestas

        return (2 * qtdArestas) / (qtdVertices * (qtdVertices - 1))

    if tipoGrafo == 1: #caso seja um grafo do tipo dígrafo
        qtdArestas = 0
        for vi in range(0, qtdVertices):
            for vj in range(vi + 1, qtdVertices):
                if matriz[vi][vj] == 1:
                    qtdArestas += 1

        return qtdArestas / (qtdVertices * (qtdVertices - 1))


'''Insere aresta: Insere uma aresta no grafo considerando o par de vértices vi e vj.
Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta inserida.
'''
def insereAresta(self, matriz, vi, vj):
    tipoGrafo = self.tipoGrafo(matriz)

    #se o grafo é do tipo dígrafo(direcionado), adicionamos o valor 1 somente na posição indicada
    #se o grafo indicado for simples, multigrafo ou pseudografo, manteremos a simetria da matriz(caso válido somente
    #para grafos não direcionados)
    if tipoGrafo == 1:
        matriz[vi][vj] = 1
    else:
        matriz[vi][vj] = 1
        matriz[vj][vi] = 1

    return matriz

'''Insere vértice: Insere um vértice no grafo.
Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice inserido.
'''
def insereVertice(matriz, vi):
    shape = matriz.shape #recebe o resultado do número de linhas e colunas da atual matriz
    novaMatriz = numpy.zeros((shape[0] + 1, shape[1] + 1)) #cria nova matriz(números zeros) com mais uma linha e coluna
    qtdVertices = np.shape(matriz)[0] #recebe a quantidade de vértices

    #a nova matriz recebe os valores da matriz antiga de acordo com as posições da iteração
    for vi in range(0, qtdVertices):
        for vj in range(0, qtdVertices):
            novaMatriz[vi][vj] = matriz[vi][vj]

    return novaMatriz

'''Remove aresta: Remove uma aresta do grafo considerando o par de vértices vi e vj.
Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam os ids dos vértices)
Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta removida.
'''
def removeAresta(self, matriz, vi, vj):
    tipoGrafo = self.tipoGrafo(matriz)

    # se o grafo é do tipo dígrafo(direcionado), adicionamos o valor 0 somente na posição indicada
    # se o grafo indicado for simples, multigrafo ou pseudografo, manteremos a simetria da matriz(caso válido somente
    # para grafos não direcionados)
    if tipoGrafo == 1:
        matriz[vi][vj] = 0
    else:
        matriz[vi][vj] = 0
        matriz[vj][vi] = 0

    return matriz

'''Remove vértice: Remove um vértice do grafo.
Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice removido.
'''
def removeVertice(matriz, vi):
    pass

