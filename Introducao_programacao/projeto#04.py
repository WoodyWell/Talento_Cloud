def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num1 == 0 or num2 == 0:
            resultado = "Não é possível dividir com o numeral zero. Tente novamente!"
        else:
            resultado = num1 / num2
    else:
        resultado = "Operação inválida. Tente novamente!"
    return resultado

print('=='*15)
print('Calculadora Experimental')
print('=='*15)
num1 = int(input('Digite o 1º valor inteiro: '))
num2 = int(input('Digite o 2º valor inteiro: '))
print('=='*15)
operacao = int(input('Escolha uma das operações abaixo: \n'
                     '[1] - Soma\n'
                     '[2] - Subtração\n'
                     '[3] - Multiplicação\n'
                     '[4] - Divisão\n'
                     'Opção escolhida: '))
print('=='*15)
print(f'Resultado: {calculadora(num1, num2, operacao)}')
