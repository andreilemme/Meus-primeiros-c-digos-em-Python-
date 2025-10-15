N = int(input("Digite um número inteiro positivo: "))

fatorial = 1
contador = 1

while contador <= N:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {N} é {fatorial}")
