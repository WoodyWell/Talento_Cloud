def calcular_tabuada(num):
    from time import sleep #importar biblioteca
    for count in range(10):
        print(f'{num} x {count+1} = {num * (count+1)}')
        sleep(1) #intervalo de 1 segundo

numero_tabuada = int(input("Tabuada do numero: ")) #solicitar número desejado pelo usuário.
calcular_tabuada(numero_tabuada)
