N = int(input("Digite um número inteiro positivo: "))

produto = 1

contador = 1
while contador <= N:
    produto *= contador
    contador += 1

print(f"O produto de todos os números de 1 a {N} é {produto}")
