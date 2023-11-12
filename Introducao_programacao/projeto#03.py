from time import sleep #Comando para importar a biblioteca time.

#Atividade utilizando o comando for.
print('Contagem dos andares utilizando o for.')
for c in range(20, 0, -1):
    if c == 13: #Condição especial para pular o número 13.
        continue
    print(f'{c}º andar')
    sleep(1) #Intervalo de 1 segundo para mostrar os andares na tela.

#Atividade utilizando o comando while.
print('=='*15)
print('Contagem dos andares utilizando o while.')
i = 20
while i != 0:
    if i != 13:
        print(f'{i}º andar')
        sleep(1)
    i -= 1
