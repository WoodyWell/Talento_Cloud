from datetime import date
ano_atual = date.today().year #Buscar ano atual automaticamente.
while True:
    try: #Tentativa de executar o código.
        nome = str(input('Digite o seu nome completo: ').upper().strip())
        ano = int(input('Digite o seu ano de nascimento: '))
        if ano >=1922 and ano <=2022: #Delimitador do ano de nascimento
            print(f'NOME COMPLETO: {nome}')
            print(f'IDADE: {ano_atual - ano}')
            print('=='*15)
            break
        else:
            print('Ano de nascimento fora do intervalo. Tente novamente!')
            print('=='*15)
    except: #Caso seja identificado erro no bloco acima.
        print('Erro! Ano digitado inválido ou campo deixado em branco... Tente novamente!')
        print('==' * 15)
