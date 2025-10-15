def numero_perfeito(n):
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n

def primeiros_numeros_perfeitos():
    numeros_perfeitos = []
    numero = 1
    while len(numeros_perfeitos) < 5:
        if numero_perfeito(numero):
            numeros_perfeitos.append(numero)
        numero += 1
    return numeros_perfeitos

numeros_perfeitos = primeiros_numeros_perfeitos()
print(f'Os 5 primeiros números perfeitos são: {numeros_perfeitos}')
