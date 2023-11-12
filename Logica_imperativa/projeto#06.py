nomeequipe = str(input('Digite o nome da equipe: ')) #Comentário: Campo para o usuário digitar o nome da equipe.

for c in range(0, 5): #Comentário: Comando "para" que vai executar um loop 5x.
    nomemembro = str(input('Digite o nome do membro: ')) #Comentário: Campo para usuário digitar o nome do membro.
    c += 1 #Comentário: Contador para adicionar o número as etiquetas.
    print(f'Etiqueta do membro {nomemembro}: {nomeequipe} - {c}') #Comentários: Mostra na tela as etiquetas de cada membro digitado.