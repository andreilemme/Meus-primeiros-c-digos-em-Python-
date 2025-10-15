N = int(input("Digite um número inteiro positivo: "))

for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
