palavras = input("Digite uma lista de palavras separadas por vírgulas: ").split(",")

palavras_unicas = sorted(set(palavras))

print("Lista de palavras sem repetições e em ordem alfabética:", palavras_unicas)
