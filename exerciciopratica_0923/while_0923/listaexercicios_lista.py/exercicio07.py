numeros = []
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

numeros_ordenados_crescente = sorted(numeros)
print("Lista em ordem crescente:", numeros_ordenados_crescente)

numeros_ordenados_decrescente = sorted(numeros, reverse=True)
print("Lista em ordem decrescente:", numeros_ordenados_decrescente)
