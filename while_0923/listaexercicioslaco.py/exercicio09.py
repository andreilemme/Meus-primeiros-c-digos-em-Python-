N = int(input("Digite um número inteiro positivo: "))

soma = 0
divisor = 1

while divisor < N:
    if N % divisor == 0:
        soma += divisor
    divisor += 1

if soma == N:
    print(f"{N} é um número perfeito")
else:
    print(f"{N} não é um número perfeito")
