from time import sleep #importando biblioteca para usar o sleep.
print('Exemplo com for')
for c in range(6):
    if c % 2 == 0: #resto da divisão para idenficar o número par.
        print(f'Regar a planta {c} - tomate')
        sleep(1) #intervalo de 1 segundo

print('=='*10)
print('Exemplo com while')
i = 0
while (i < 6):
    if i % 2 == 0: #resto da divisão para idenficar o número par.
        print(f'Regar a planta {i} - tomate')
        sleep(1) #intervalo de 1 segundo
    i += 1

from time import sleep #importando biblioteca para usar o sleep.
print('Regando as plantas de trás pra frente utilizando o for in range.')
for c in range(5,0,-1): #utilizando o range com o passo -1
    print(f'Regar a planta {c}')
    sleep(1) #intervalo de 1 segundo para cada print