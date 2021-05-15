import os.path
from os import path

def pede_nome():

    print('Introduza o nome do FILE')
    nome = input()

    while not path.exists(nome):
        print("File exists:" + str(path.exists('nome')))
        print('Introduza o nome do FILE')
        nome = input()

    print('Nome do ficheiro = ' + nome)

def gera_nome(filename):

    filename.split('.')
    file = filename[0]+'.json'
    print (file)
    return  file
