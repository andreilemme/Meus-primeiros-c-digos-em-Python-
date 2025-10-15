decimal = int(input("Digite um número decimal: "))

binario = ""

while decimal > 0:
    resto = decimal % 2
    binario = str(resto) + binario
    decimal = decimal // 2

print(f"O número binário é: {binario}")
