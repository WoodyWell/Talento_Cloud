from time import sleep #importando biblioteca para usar o sleep.

print('Atividade #3: Regando apenas as batatas (3, 4 e 5).')
for c in range(3, 6): #utilizando o range no intervalo 3 ~ 6
    print(f'Regar a planta {c}')
    sleep(1) #intervalo de 1 segundo para cada print
print('Parabéns! Você regou todas as batatas.')

print('=='*15)

print('Atividade #4: Regando apenas os tomates (0, 1, 4 e 5).')
for c in range(0, 6): #utilizando o range no intervalo 0 ~ 6
    if c == 2 or c == 3: #condição para desconsiderar as plantas 2 e 3
        continue
    else:
        print(f'Regar a planta {c}')
    sleep(1) #intervalo de 1 segundo para cada print
print('Parabéns! Você regou todos os tomates.')

print('=='*15)

print('Atividade #5: Regando as plantas de trás pra frente.')
for c in range(5, 0, -1): #utilizando o range com o passo -1
    print(f'Regar a planta {c}')
    sleep(1) #intervalo de 1 segundo para cada print
print('Parabéns! Você regou todas as plantas de trás pra frente.')