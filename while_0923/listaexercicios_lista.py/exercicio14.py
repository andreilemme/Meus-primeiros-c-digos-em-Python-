quantidade = int(input("Quantas palavras você deseja inserir? "))

palavras = []
for i in range(quantidade):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)

contagem = sum(1 for palavra in palavras if len(palavra) > 5)

print("Quantidade de palavras com mais de 5 letras:", contagem)
