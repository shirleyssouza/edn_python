respostaUsuario = input("Você precisa enciar um pacote? (Digite 'sim' ou 'não') ")

if respostaUsuario == "sim":
    print("Podemos te ajudar a enviar o pacote!")
else:
    print("Volte quando precisar enviar um pacote. Obrigada!")
    
#######################################################################

respUsuario = input("Você gostaria de comprar selos, comprar um envelope ou fazer uma cópia (Digite selos, envelope ou copia)? ")

if respUsuario == "selos":
    print("Temos muitos desingn de selos para escolher.")
elif respUsuario == "envelope":
    print("Temos muitos tamanhos de envelopes para escolher.")
elif respUsuario == "copia":
    quantidade = input("Quantas cópias você gostaria (Digite um número)? ")
    print(f"Aqui estão suas {quantidade} cópias")
else:
    print("Obrigado, volte sempre.")