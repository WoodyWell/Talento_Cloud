#lista com 5 produtos de uma loja de música.
albuns = ['Ten - Pearl Jam', 'A Rush of Blood to The Head - Coldplay', 'Use Your Illusion II - Guns N Roses', 'Is This It - The Strokes', 'Wish You Were Here - Pink Floyd']
print('Lista de álbuns:')
print(albuns)
print('=='*35)

print('Lista de álbuns (utilizando o for):')
num = 0
for album in albuns:
    num += 1
    print(f'{num} - {album}')
print('=='*35)

#lista com anos de nascimento de familiares e amigos.
ano_nascimento = [1971, 1974, 1994, 1996, 2002]
print('Lista com os anos de nascimento de familiares e amigos:')
print(ano_nascimento)
print('=='*35)

print('Lista com os anos de nascimento de familiares e amigos (utilizando o for):')
num2 = 0
for ano in ano_nascimento:
    num2 += 1
    print(f'{num2} - {ano}')
print('=='*35)