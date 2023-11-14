from time import sleep #importando biblioteca para usar o sleep.
print('Regando as plantas de trás pra frente utilizando o for in range.')
for c in range(5,0,-1): #utilizando o range com o passo -1
    print(f'Regar a planta {c}')
    sleep(1) #intervalo de 1 segundo para cada print