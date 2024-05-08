from table import Tabela_Verdade
from time import sleep

#Função principal;
def main():
    variaveis = ['A', 'B']
    while True:
        try:
            operacao = str(input('Digite a operação que deseja realizar (AND, OR, NOT): ')).upper().strip()
            if operacao == '':
                raise KeyboardInterrupt

            if operacao not in ['AND', 'OR', 'NOT']:
                print('Operação inválida!')
                break

            tabela = Tabela_Verdade(variaveis, operacao)
            print('Tabela verdade sendo gerada.')
            sleep(1)
            print('Aguarde alguns segundos...')
            sleep(1)
            tabela.gerador_tabela()
            break

        except KeyboardInterrupt:
            print('\nNenhuma operação lógica digitada.')
            break

        except ValueError as e:
            print(e)
            break


if __name__ == "__main__":
    main()