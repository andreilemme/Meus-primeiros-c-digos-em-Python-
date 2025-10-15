numeros = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

positivos = [num for num in numeros if num > 0]
negativos = [num for num in numeros if num < 0]

print("Números positivos:", positivos)
print("Números negativos:", negativos)
