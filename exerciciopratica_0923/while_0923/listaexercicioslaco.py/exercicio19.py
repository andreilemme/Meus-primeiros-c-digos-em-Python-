N = int(input("Digite um número inteiro positivo: "))

def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

soma_fatoriais = 0

for i in range(1, N + 1):
    soma_fatoriais += fatorial(i)

print(f"A soma dos fatoriais de 1 até {N} é {soma_fatoriais}")
