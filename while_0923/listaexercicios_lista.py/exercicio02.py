numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("O maior número é:', maior")
print("O menor número é:", menor)
