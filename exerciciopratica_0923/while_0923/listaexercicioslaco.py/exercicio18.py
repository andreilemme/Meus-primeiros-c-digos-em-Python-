N = int(input("Digite um número inteiro positivo: "))

soma = 0.0

for i in range(1, N + 1):
    soma += 1 / i

print(f"A soma da série é {soma:.4f}")
