frutas = ["maçã", "banana", "laranja", "pera", "uva"]

fruta_digitada = input("Digite o nome de uma fruta: ")

mensagem = "está na lista." if fruta_digitada in frutas else "não está na lista."
print(f"A fruta {fruta_digitada} {mensagem}")
