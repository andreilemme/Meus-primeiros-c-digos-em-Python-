numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_impares = 0

for num in numeros:
    if num % 2 != 0:
        soma_impares += num
print("A soma dos números ímpares é:", soma_impares)
