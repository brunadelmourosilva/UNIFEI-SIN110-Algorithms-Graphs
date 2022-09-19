'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma lista de adjacências.

18/09/2022
===================================================='''

import numpy as np
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)

'''Tipo do grafo: Retorna o tipo do grafo representado por uma dada lista de adjacências.
Entrada: lista de adjacências (tipo Dictionary)
Saída: Integer (0 – simples; 1 – dígrafo; 2 – multigrafo; 3 – pseudografo)
'''
def tipoGrafo(listaAdjacencia):
    diagonalEhZerada = True
    numerosLimitadosAZeroOuUm = True
    matrizAssimetrica = True

    #converte lista de adjacência para uma matriz de adjacência
    matrizAdjacencia = converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia)

    # retorna a quantidade chaves do dicionário(vértices) do grafo
    qtdVertices = np.shape(matrizAdjacencia)[0]

    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(vi + 1, qtdVertices):  # Para cada vértice vj
            if vi == vj:
                if matrizAdjacencia[vi][vj] != 0: #caso a diagonal possua valores diferentes de 0
                    diagonalEhZerada = False

            if matrizAdjacencia[vi][vj] > 1: #caso a matriz possua valores maiores que 1
                numerosLimitadosAZeroOuUm = False

            if matrizAdjacencia[vi][vj] == matrizAdjacencia[vj][vi]: #caso onde a posição dada e sua inversa sejam iguais
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
Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos números inteiros que indica o id do vértice)
Saída: Boolean (True se os vértices são adjacentes; False caso contrário)
'''
def verificaAdjacencia(listaAdjacencia, vi, vj):
    #converte lista de adjacência para uma matriz de adjacência
    matrizAdjacencia = converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia)

    if matrizAdjacencia[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes)

    return verticesAdjacentes


'''Calcula densidade: Retorna o valor da densidade do grafo.
Entrada: lista de adjacências (tipo Dictionary)
Saída: Float (valor da densidade com precisão de três casas decimais)
'''
def calcDensidade(self, listaAdjacencia):
    #converte lista de adjacência para uma matriz de adjacência
    matrizAdjacencia = converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia)

    #recebe o tipo do grafo para que a escolha do cálculo seja de acordo com o tipo retornado
    tipoGrafo = self.tipoGrafo(listaAdjacencia)

    qtdVertices = np.shape(matrizAdjacencia)[0]

    if tipoGrafo == 0: #caso seja um grafo do tipo simples
        qtdArestas = 0
        for vi in range(0, qtdVertices):
            for vj in range(vi + 1, qtdVertices):
                if matrizAdjacencia[vi][vj] == 1: #se a posição for 1, significa que possui aresta
                    qtdArestas += 1 #realiza o calculo da quantidade de arestas

        return (2 * qtdArestas) / (qtdVertices * (qtdVertices - 1))

    if tipoGrafo == 1: #caso seja um grafo do tipo dígrafo
        qtdArestas = 0
        for vi in range(0, qtdVertices):
            for vj in range(vi + 1, qtdVertices):
                if matrizAdjacencia[vi][vj] == 1:
                    qtdArestas += 1

        return qtdArestas / (qtdVertices * (qtdVertices - 1))


'''Insere aresta: Insere uma aresta no grafo considerando o par de vértices vi e vj.
Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam o id do vértice)
Saída: lista de adjacências (tipo Dictionary) com a aresta inserida.
'''
def insereAresta(self, listaAdjacencia, vi, vj):
    #converte lista de adjacência para uma matriz de adjacência
    matrizAdjacencia = converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia)

    #recebe o tipo do grafo para que a escolha da inserção da aresta seja de acordo com o tipo retornado
    tipoGrafo = self.tipoGrafo(listaAdjacencia)

    #se o grafo é do tipo dígrafo(direcionado), adicionamos o valor 1 somente na posição indicada
    #se o grafo indicado for simples, multigrafo ou pseudografo, manteremos a simetria da matriz(caso válido somente
    #para grafos não direcionados)
    if tipoGrafo == 1:
        matrizAdjacencia[vi][vj] = 1
    else:
        matrizAdjacencia[vi][vj] = 1
        matrizAdjacencia[vj][vi] = 1

    #criando um novo grafo para a visualização da nova aresta
    G = g.criaGrafo(matrizAdjacencia)
    vis.visualizarGrafo(True, G, "aresta inserida")

    return ds.criaListaAdjacencias(matrizAdjacencia)

'''Insere vértice: Insere um vértice no grafo.
Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
Saída: lista de adjacências (tipo Dictionary) com o vértice inserido.
'''
def insereVertice(listaAdjacencia, vi):
    #converte lista de adjacência para uma matriz de adjacência
    matrizAdjacencia = converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia)

    #recebe o resultado do número de linhas e colunas da atual matriz
    shape = len(matrizAdjacencia)

    #cria nova matriz(números zeros) com mais uma linha e coluna
    novaMatriz = np.zeros((shape + 1, shape + 1))

    #recebe a quantidade de vértices
    qtdVertices = np.shape(matrizAdjacencia)[0]

    #a nova matriz recebe os valores da matriz antiga de acordo com as posições da iteração
    for vi in range(0, qtdVertices):
        for vj in range(0, qtdVertices):
            novaMatriz[vi][vj] = matrizAdjacencia[vi][vj]

    #criando um novo grafo para a visualização do novo vértice
    G = g.criaGrafo(novaMatriz)
    vis.visualizarGrafo(True, G, "vértice inserido")

    return ds.criaListaAdjacencias(novaMatriz)

'''Remove aresta: Remove uma aresta do grafo considerando o par de vértices vi e vj.
Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam os ids dos vértices)
Saída: lista de adjacências (tipo Dictionary) com a aresta removida.
'''
def removeAresta(self, listaAdjacencia, vi, vj):
    # converte lista de adjacência para uma matriz de adjacência
    matrizAdjacencia = converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia)

    # recebe o tipo do grafo para que a escolha da inserção da aresta seja de acordo com o tipo retornado
    tipoGrafo = self.tipoGrafo(listaAdjacencia)

    # se o grafo é do tipo dígrafo(direcionado), adicionamos o valor 0 somente na posição indicada
    # se o grafo indicado for simples, multigrafo ou pseudografo, manteremos a simetria da matriz(caso válido somente
    # para grafos não direcionados)
    if tipoGrafo == 1:
        matrizAdjacencia[vi][vj] = 0
    else:
        matrizAdjacencia[vi][vj] = 0
        matrizAdjacencia[vj][vi] = 0

    G = g.criaGrafo(matrizAdjacencia)
    vis.visualizarGrafo(True, G, "aresta removida")

    return ds.criaListaAdjacencias(matrizAdjacencia)

'''Remove vértice: Remove um vértice do grafo.
Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice removido.
'''
def removeVertice(matriz, vi):
    pass

'''Converte uma lista de adjacência para uma matriz de adjacência.
Entrada: lista de adjacência
Saída: matriz de adjacências
'''
def converteListaAdjacenciaParaMatrizAdjacencia(listaAdjacencia):
    # retorna a quantidade chaves do dicionário(vértices) do grafo
    qtdVertices = len(listaAdjacencia)

    #inicializa a matriz
    matrizAdjacencia = [[0 for j in range(qtdVertices)]
              for i in range(qtdVertices)]

    for i in range(qtdVertices):
        for j in listaAdjacencia[i]:
            matrizAdjacencia[i][j] += 1

    return matrizAdjacencia
