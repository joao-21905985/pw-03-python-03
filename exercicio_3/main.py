import os


def pede_pasta():
    while True:
        currentPath = os.getcwd()
        path = input("Insira path:\n")
        if os.path.exists(path):
            return path
        else:
            addPath = os.path.join(currentPath , path)
            if os.path.exists(addPath):
                return addPath


def calc_tamanho_pasta (path):
    tamPasta = 0
    listFileFolder = os.listdir(path)

    for file in listFileFolder:

        if os.path.isfile( os.path.join(path , file)):
            f_path = os.path.join(path , file)
            tamPasta += os.path.getsize(f_path)
        elif os.path.isdir( os.path.join(path , file)):
            tamPasta += calc_tamanho_pasta( os.path.join(path , file))

    return tamPasta

def main():
    path = pede_pasta()
    print(f"Tamanho ->> {calc_tamanho_pasta(path)}")

if __name__ == "__main__":
    main()