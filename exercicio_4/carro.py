menu = '                              Menu do Carro                         \n' \
       ' -> combustivel: imprime a quantidade de combustível no depósito\n' \
       ' -> autonomia: imprime o numero de Km que é possível percorrer com o combustível no depósito\n' \
       ' -> abastece: enche o valor inserido de litros no tanque do carro\n' \
       ' -> percorre: percorre o caminho inserido em Kms\n'

class automovel:

    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return (self.quant_comb * 100 ) / self.consumo

    def abastece(self, litros):
        if self.quant_comb + litros <= self.cap_dep:
            self.quant_comb += litros
            print(f'O tanque tem {self.quant_comb} litros de combustível')
        else:
            print(
                f'Tentou abastecer demasiado, limite máximo de {self.cap_dep - self.quant_comb} litros')

    def percorre(self, km):
        if km <= self.autonomia():
            gasto_combustivel = (km * self.consumo) / 100
            self.quant_comb -= gasto_combustivel
            print(f'Foram percorridos os {km} Kms e foram consumidos {gasto_combustivel}  litros de combustível')
        else:
            print(
                f'Nao é possivel percorrer o trajeto pedido, com o combustivel do carro. O carro tem uma autonomia de {self.autonomia()} Kms apenas')

def is_float(str_input):
        try:
            float(str_input)
            return True
        except:
            return False

def get_float_input(output):
        while not is_float(variable := input(output)):
            print('Input inválido')
        return float(variable)

def main():
    cap_dep = get_float_input('Insira a capacidade do depósito do tanque do carro em litros: ')
    quant_comb = get_float_input('Insira a quantidade de combustível no tanque do carro em litros: ')
    consumo = get_float_input('Insira a quantidade de litros gastos a cada 100 kms: ')
    print("\n\n")
    carro = automovel(cap_dep, quant_comb, consumo)
    while (option := input(menu)) != 'quit':
        if option == 'combustivel':
            print(f'Neste momento tem {carro.combustivel()} litros no tanque.')
        elif option == 'autonomia':
            print(f'Neste momento ainda pode percorrer {carro.autonomia()} Kms.')
        elif option == 'abastece':
            num_litros = get_float_input('Insira a quantidade de combustivel que pretende abastecer em litros: ')
            carro.abastece(num_litros)
        elif option == 'percorre':
            num_kms = get_float_input('Insira a quantidade de Kms que pretende percorrer: ')
            carro.percorre(num_kms)
        elif option != 'quit':
            print('Opção inválida, tente novamente')

if __name__ == "__main__":
        main()

