def numero_perfeito(n):
    soma_divisores = 0
    
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    
    if soma_divisores == n:
        return True
    else:
        return False

numero = 6
if numero_perfeito(numero):
    print(f'O número {numero} é perfeito.')
else:
    print(f'O número {numero} não é perfeito.')

numero = 28
if numero_perfeito(numero):
    print(f'O número {numero} é perfeito.')
else:
    print(f'O número {numero} não é perfeito.')

numero = 15
if numero_perfeito(numero):
    print(f'O número {numero} é perfeito.')
else:
    print(f'O número {numero} não é perfeito.')
