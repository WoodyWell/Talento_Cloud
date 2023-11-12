#Comentário: Bloco apenas para simular a experiência de um restaurante.
print('=='*13)
print('RESTAURANTE BUCHO CHEIO')
print('=='*13)
print('Sejam bem-vindos!')
print('Precisarei realizar algumas perguntas para saber o melhor local para acomodá-los.')
print('=='*13)

#Comentário: Bloco com a entrada das informações e inserção dos valores nas variáveis.
qtd_pessoas = int(input('Mesa para quantas pessoas? '))
fumante = str(input('Alguém do grupo é fumante? [S/N]: ').upper())
animais = str(input('Há animais de estimação? [S/N]: ').upper())

#Comentário: Bloco apenas para simular a experiência de um restaurante.
print('=='*13)
print('Obrigado pelas respostas. Estou verificando o melhor local para vocês...')
print('=='*13)

#Comentário: Bloco de processamento e saída dos dados, verificando através das condições a melhor solução.
if fumante == 'S' or animais == 'S':
    print('A área externa é ideal para vocês!')
elif qtd_pessoas >= 5:
    print('O ideal para vocês é uma mesa no 1º andar pois não é possível juntar mesas no térreo!')
else:
    print('Tenho uma mesa perfeita pra vocês no térreo!')

#Comentário: Final do algoritmo.
print('Fiquem à vontade!')