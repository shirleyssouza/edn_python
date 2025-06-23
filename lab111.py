# listas, são editaveis e se caracterizam por serem escritas dentro de colchetes
fruta = ["maçã", "banana", "laranja"]
print(fruta)
print(type(fruta))

print(fruta[0])
print(fruta[2])
print(fruta[-1])

fruta[0] = "abacaxi"
print(fruta)

# tuplas, são IMUTAVEIS e se caracterizam por serem escritas dentro de parentesis
fruta = ("maçã", "banana", "laranja")
print(fruta)
print(type(fruta))

print(fruta[0])
print(fruta[2])
print(fruta[-1])

# Dicinarios
fruta = {"Ricardo": "Maçã",
         "Shirley": "Melancia",
         "Jaidete": "Manga"        
}
print(fruta)
print(type(fruta))
print(fruta["Ricardo"])
print(fruta["Shirley"])