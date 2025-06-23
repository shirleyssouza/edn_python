#Cria uma lista cahamada "listaMista" com diferentes tipos de dados
listaMista = [45, 290578, 1.02, True, "Meu cachorro está na cama", "45"]

#Inicia um loop "for" que percorre cada elemento da lista
for item in listaMista:
    print(f'{item} é do tipo de dado {type(item)}')