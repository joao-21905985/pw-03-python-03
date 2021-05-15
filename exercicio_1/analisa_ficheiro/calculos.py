
def calcula_linhas(nomeFile):

    f =open(nomeFile,'r')
    count = 0

    for line in f :
        if line != '\n':
            count +=1

    f.close()

    return count


def calcula_caracteres(filename):

    f=open(filename,'r')

    str = f.read()
    count = len(str)
    print(count)
    count -= calcula_linhas(filename) -1

    f.close()
    print (f"O File tem {count} chars ")

def calcula_palavra_comprida(filename):

    sizeWord=0
    maiorWord=''

    f=open(filename,'r')

    for line in f :
        for i in line.split(' '):
            if len(i)> sizeWord :
                sizeWord = len(i)
                maiorWord = i

    print(f"A maior palavra ->> {maiorWord} e tem tamanho {sizeWord}")



