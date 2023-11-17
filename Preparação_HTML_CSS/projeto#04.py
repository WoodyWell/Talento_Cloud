from time import sleep #importando biblioteca
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
lista_produtos[1] = 'rímel'
lista_produtos[4] = 'cremes hidratantes'
lista_produtos.pop()

print('ATENÇÃO! NOVOS PRODUTOS DISPONÍVEIS!')
for itens in lista_produtos:
    print(f'Temos {itens} à venda!')
    sleep(2) #intervalo de 2 segundos pra cada produto.
