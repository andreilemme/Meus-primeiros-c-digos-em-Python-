palavras = ["maçã", "banana", "laranja", "uva", "melancia"]

palavra = input("Digite uma palavra: ")

if palavra in palavras:
    print("A palavra já está na lista.")
else:
    palavras.append(palavra)
    print("A palavra foi adicionada à lista.")

print("Lista atualizada:", palavras)
