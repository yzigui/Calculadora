import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '**':
        result = num1 ** num2
    elif operador == '%':
        result = num1 % num2

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            print('Calculadora')
            print('----------------------------------')
            print('+  Soma')
            print('-  Subtração')
            print('*  Multiplicação')
            print('/  Divisão')
            print('** Exponenciação')
            print('%  Módulo')
            print('----------------------------------\n')

            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            operador = input('Digite a operação: ')

            resultado = calculadora(num1, num2, operador)

            print(f'\nResultado: {resultado}')

            continuar = input('\nDeseja realizar outra operação? (s/n): ')

            if continuar.lower() != 's':
                break

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')