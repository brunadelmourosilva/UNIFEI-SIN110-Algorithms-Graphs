'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

18/09/2022

Aluno(a): Bruna Delmouro da Silva - 2021001809
===================================================='''
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from class_4.grafo import caracteristicas as car

'''Core do programa'''
def main(instancia):
    matriz = ds.criaMatrizAdjacencias(instancia) #cria matriz de adjacência
    listaAdjacencia = ds.criaListaAdjacencias(matriz) #cria lista de adjacência

    # print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando
    G = g.criaGrafo(matriz)
    print(G, '\n') # Mostra as características do grafo.

    vis.visualizarGrafo(True, G, instancia)  # True para visualização do grafo ou False.

    ### FUNÇÃO 1 ###
    funcao1 = car.tipoGrafo(listaAdjacencia)
    print('Tipo do grafo: {}\n'.format(funcao1))

    resultado = [instancia, funcao1]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado, instancia)  # Salva resultado em arquivo

    ### FUNÇÃO 2 ###
    funcao2 = car.verificaAdjacencia(listaAdjacencia, 0, 1)

    resultado = [instancia, funcao2]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 3 ###
    funcao3 = car.calcDensidade(car, listaAdjacencia)
    print('Densidade do grafo: {:.3f}\n'.format(funcao3))

    resultado = [instancia, funcao3]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 4 ###
    linha = 1
    coluna = 2
    print('Insere aresta na posição {}x{}: \n'.format(linha, coluna))

    funcao4 = car.insereAresta(car, listaAdjacencia, linha, coluna)

    resultado = [instancia, funcao4]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 5 ###
    print('Insere vértice:')
    funcao5 = car.insereVertice(listaAdjacencia, 1)

    resultado = [instancia, funcao5]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 6 ###
    linha = 1
    coluna = 2
    print('Remove aresta na posição {}x{}: \n'.format(linha, coluna))

    funcao6 = car.removeAresta(car, funcao5, linha, coluna)

    resultado = [instancia, funcao6]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 7 ###
    # vi = 6
    # funcao7 = car.removeVertice(matriz, vi)
    # print('Remove vértice: \n {} \n'.format(funcao7))
    #
    # G = g.criaGrafo(funcao7)
    # vis.visualizarGrafo(True, G, instancia + " - remove vértice")
    #
    # resultado = [instancia, funcao7]
    # ds.salvaResultado(resultado, instancia)

    

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str('exemplo')) #substituir por sys.argv[1]