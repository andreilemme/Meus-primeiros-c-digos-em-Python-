num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = 0

for _ in range(num2):
    resultado += num1

print(f"{num1} multiplicado por {num2} é {resultado}")
