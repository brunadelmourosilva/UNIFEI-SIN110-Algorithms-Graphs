import numpy as np
import os

def write_file(inst, result):
    # creating a file path to write a file of according the instance and result passed on parameter
    path = '{}/outputs/{}_result.txt'.format(os.getcwd(), inst)

    # local where the file will be created
    file = open(path, "w")

    # the file will be emptied before the text will be inserted at the current file
    file.write(str(result))

    # close the file after writing
    file.close()

    # print string result on console
    print(result)

def read_file(inst):
    # creating a file path to read the file of according the instance passed on parameter
    path = '{}/datasets/{}.txt'.format(os.getcwd(), inst)

    # loading the file and storage in a matrix of the type 'numpy'
    load_file = np.loadtxt(path)

    # getting the array's dimension by 'shape' method and this method will return a tuple
    shape = load_file.shape

    # format results in a string
    result = 'nome da instância: {} | quantidade de linhas: {} | quantidade de colunas: {}'.format(inst, shape[0], shape[1])

    return result

def run_methods(inst):
    result = read_file(inst)
    write_file(inst, result)