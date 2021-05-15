from matplotlib import pyplot as plt
import os
import csv


def pede_pasta():
    nome = input ("Introduza o caminho da pasta\n")
    return nome

def faz_calculos(nome):
    typesOfFiles = []
    sizePasta = {}
    listFiles = os.listdir(nome)

    for file in listFiles:
        if len(file.split('.')) > 1 :
            typesOfFiles.append(f"{file.split('.')[1]}") # extrair a extenão do file

    for typeFile in set(typesOfFiles):
        f_size = 0

        for file in listFiles:
            if len(file.split('.')) > 1:
                if file.split('.')[1] == typeFile:
                    f_path = os.path.join(nome, file)
                    f_size += os.path.getsize(f_path) #dividir 1024 ? ou deixar estar ?

        count_types = sum([1 for type in typesOfFiles if typeFile == type])
        sizePasta[typeFile] = [f"volume: {f_size}", f"quantidade:{count_types}"]

    return sizePasta

def guarda_resultados (resultados, nome):
    CsvFileName = (nome.split('\\')[-1]) #dividir o directorio por //
    with open (f"{CsvFileName}.csv", "w" , newline = '') as ficheiro:
        campos = ['Extensao','Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames = campos)
        writer.writeheader()
        for type, calculos in resultados.items():
            writer.writerow({'Extensao': f"{type}", 'Quantidade': calculos[1].split(':')[1],
                             'Tamanho[kByte]': calculos[0].split(':')[1]})


def faz_grafico_queijos (titulo, resultados):
    listValues = []
    for resultado in resultados.values():
        listValues.append([resultado[0].split(':')[1]])
    plt.pie(listValues, labels=resultados.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, resultados):
    listValues = []
    listKeys = []

    for item in sorted(resultados, key=resultados.get):
        listKeys.append(item)
        listValues.append(resultados.get(item)[0].split(':')[1])

    plt.bar(listKeys, listValues)
    plt.title(titulo)
    plt.show()
