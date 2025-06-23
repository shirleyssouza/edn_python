import random

print("Bem-vindo ao jogo Adivinhe o Número!")
print("As regras são simples. Eu vou pensar em um número, e você tentará adivinhar.")
number = random.randint(1, 10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Adivinhe um número de 1 a 10: ")
    if int(guess) == number:
        print("Você digitou {}. Isso está correto! Você venceu!".format(guess))
        isGuessRight = True
    else:
        print("Você digitou {}. Desculpe, não é esse número. Tente outra vez.".format(guess))
        
###############################################################################################

print("Contador de número de 1 a 10!")
for i in range(1, 11):
    print(i, end=" ")