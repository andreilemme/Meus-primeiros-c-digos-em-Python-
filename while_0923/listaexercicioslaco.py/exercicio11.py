N = int(input("Digite um número inteiro positivo: "))

soma = 0

contador = 1
while contador <= N:
    if contador % 2 == 0: 
        soma += contador
    contador += 1

print(f"A soma de todos os números pares de 1 a {N} é {soma}")
