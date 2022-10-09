
from Metodos import (caracteristicas as car)
from Inicializacao import (dataSet as ds)

def main(instancia):
    matriz = ds.criaMatrizAdjacencias(instancia)
    #car.warshall(matriz)

    car.caminhoEuleriano(matriz)


if __name__ == '__main__':
    main(str('teste'))