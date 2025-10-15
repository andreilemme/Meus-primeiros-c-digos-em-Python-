numeros_str = input("Digite uma lista de números separados por vírgulas: ")

numeros = [int(num) for num in numeros_str.split(",")]

media = sum(numeros) / len(numeros)

print("A média dos números da lista é:", media)
numeros = input("Digite uma lista de números separados por vírgula: ")

numeros_lista = []
for numero in numeros.split(","):
    if numero.strip().isdigit():
        numeros_lista.append(int(numero.strip()))
    else:
        print("A entrada contém valores não numéricos. Por favor, tente novamente.")
        numeros_lista = []
        break

if numeros_lista:
    soma = 0
    contador = 0
    while contador < len(numeros_lista):
        soma += numeros_lista[contador]
        contador += 1
    media = soma / len(numeros_lista)
    print("A média dos números é:", media)
else:
    print("Nenhuma média a ser calculada.")
