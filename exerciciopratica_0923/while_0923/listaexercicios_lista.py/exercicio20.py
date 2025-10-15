numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)


resultado = []
for numero in numeros:
    if numero % 2 == 0:
        resultado.append(numero ** 2)  
    else:
        resultado.append(numero ** 3)  


print("Lista original:", numeros)
print("Lista modificada:", resultado)