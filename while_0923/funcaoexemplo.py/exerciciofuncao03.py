#Faça um programa em Python, que tenha uma função
#que receberá 3 valores com parâmetro e que 
#exiba a soma destes três valores.
def soma_tres_valores(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    print("A soma dos três valores é:", soma)

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor"))

soma_tres_valores(v1, v2, v3)

#Exemplo do professor:
def somarValores(v1, v2, v3):
    soma = v1+v2+v3
    print(f"A soma de {v1}+{v2}+{v3}={soma}")

somarValores(5,7,9)
somarValores(3.3,56,2.2)
