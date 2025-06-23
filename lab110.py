mensagem = "Isso é uma string"
print(type(mensagem))
print(type(mensagem))
print(mensagem + " is of the data type " + str(type(mensagem)))
print(f'{mensagem} is of the data type {str(type(mensagem))}')

primeiroNome = "Shirley"
segundoNome = "Souza"
nomeCompleto = primeiroNome + " " + segundoNome
print(nomeCompleto)

nome = input("Qual o seu nome? ")
cor = input("Qual sua cor favorita? ")
animal = input("Qual seu animal favorito? ")
print("{}, gosta da cor {} e do animal {}.".format(nome, cor, animal)) #não se usa mais, deve usar o fString