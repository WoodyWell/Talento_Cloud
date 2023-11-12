print('Características do veículo desejado. ')
qtd_rodas = int(input('Digite a quantidade de rodas: '))
peso_bruto = int(input('Digite o peso bruto do veículo em kg: '))
qtd_pessoas = int(input('Digite a quantidade de pessoas: '))
habilitacao = str()

if qtd_rodas == 2 or qtd_rodas == 3:
    habilitacao = "A"
elif qtd_rodas >= 4:
    if qtd_pessoas <= 8 and peso_bruto <= 3500:
        habilitacao = "B"
    elif peso_bruto >= 3500 and peso_bruto <= 6000:
        habilitacao = "C"
    elif qtd_pessoas > 8:
        habilitacao = "D"
    elif peso_bruto > 6000:
        habilitacao = "E"
else:
    habilitacao = "Parâmetro não programado, favor tentar novamente..."

print(f'De acordo com os parâmetros analisados, a melhor categoria é: {habilitacao}')
