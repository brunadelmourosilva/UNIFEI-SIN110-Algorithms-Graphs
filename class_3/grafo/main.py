'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

05/09/2022
===================================================='''
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from Metodos import (caracteristicas as car)

'''Core do programa'''
def main(instancia):
    matriz = ds.criaMatrizAdjacencias(instancia)
    print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    G = g.criaGrafo(matriz)
    print(G, '\n') # Mostra as características do grafo.

    vis.visualizarGrafo(True, G, instancia)  # True para visualização do grafo ou False.

    ### FUNÇÃO 1 ###
    funcao1 = car.tipoGrafo(matriz)
    print('Tipo do grafo: {}\n'.format(funcao1))

    resultado = [instancia, funcao1]  # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado, instancia)  # Salva resultado em arquivo

    ### FUNÇÃO 2 ###
    funcao2 = car.verificaAdjacencia(matriz, 0, 1)

    resultado = [instancia, funcao2]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 3 ###
    funcao3 = car.calcDensidade(car, matriz)
    print('Densidade do grafo: {}\n'.format(funcao3))

    resultado = [instancia, funcao3]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 4 ###
    linha = 1
    coluna = 2
    funcao4 = car.insereAresta(car, matriz, linha, coluna)
    print('Insere aresta na posição {}x{}: \n {} \n'.format(linha, coluna, funcao4))

    #criando um novo grafo para a visualização da nova aresta
    G = g.criaGrafo(funcao4)
    vis.visualizarGrafo(True, G, instancia + " - insere aresta")

    resultado = [instancia, funcao4]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 5 ###
    funcao5 = car.insereVertice(matriz, 1)
    print('Insere vértice: \n {} \n'.format(funcao5))

    # criando um novo grafo para a visualização da nova aresta
    G = g.criaGrafo(funcao5)
    vis.visualizarGrafo(True, G, instancia + " - insere vértice")

    resultado = [instancia, funcao5]
    ds.salvaResultado(resultado, instancia)

    ### FUNÇÃO 6 ###
    linha = 1
    coluna = 2
    funcao6 = car.removeAresta(car, funcao5, linha, coluna)
    print('Remove aresta: \n {} \n'.format(funcao6))

    G = g.criaGrafo(funcao6)
    vis.visualizarGrafo(True, G, instancia + " - remove aresta")

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