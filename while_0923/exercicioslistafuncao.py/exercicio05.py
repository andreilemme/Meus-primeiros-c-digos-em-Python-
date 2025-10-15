def numero_divisores(valor):
    if valor <= 0:
        return "O valor deve ser um número inteiro positivo."
    
    contador = 0
    for i in range(1, valor + 1):
        if valor % i == 0:
            contador += 1
    return contador

numero = 12
print(f'O número de divisores de {numero} é {numero_divisores(numero)}') 

numero = 25
print(f'O número de divisores de {numero} é {numero_divisores(numero)}') 
