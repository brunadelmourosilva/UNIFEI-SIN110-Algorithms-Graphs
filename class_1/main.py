import numpy as np
import os

def write_file(inst, result):
    path = '{}\outputs\{}_result.csv'.format(os.getcwd(), inst)

    file = open(path, "w")
    file.write(str(result))
    file.close()

def read_file(inst):
    #create file path to read the file
    path = '{}\datasets\{}.txt'.format(os.getcwd(), inst)

    #load the file and storage in a matrix kind of 'numpy'
    file_load = np.loadtxt(path)

    #the array's dimension by shape() method
    shape = file_load.shape

    #save file in a new directory
    # todo return a format string
    write_file(inst, shape)

    #todo return a format string
    return shape


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(read_file('zachary'))
