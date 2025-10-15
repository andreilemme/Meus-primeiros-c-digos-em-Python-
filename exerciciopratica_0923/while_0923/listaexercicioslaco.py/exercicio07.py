N = int(input("Digite um número inteiro positivo: "))

a, b = 0, 1
contador = 0

while contador < N:
    print(a)
    a, b = b, a + b
    contador += 1
