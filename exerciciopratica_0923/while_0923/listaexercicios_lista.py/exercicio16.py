numeros = []
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

esta_crescente = all(numeros[i] <= numeros[i + 1] for i in range(len(numeros) - 1))

if esta_crescente:
    print("A lista está em ordem crescente.")
else:
    print("A lista não está em ordem crescente.")
