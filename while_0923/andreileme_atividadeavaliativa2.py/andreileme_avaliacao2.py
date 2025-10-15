def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

def separar_primos(numeros):
    """Separa os números em primos e não primos."""
    primos = []
    nao_primos = []
    for numero in numeros:
        if eh_primo(numero):
            primos.append(numero)
        else:
            nao_primos.append(numero)
    return primos, nao_primos

def entrada_valida(entrada):
    """Verifica se a entrada é um número inteiro válido."""
    if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
        return True
    return False

lista_numeros = []

print("Digite números inteiros para adicionar à lista. Digite 0 para finalizar.")
while True:
    entrada = input("Digite um número: ")
    
    if entrada_valida(entrada):
        numero = int(entrada)
        if numero == 0:
            break
        lista_numeros.append(numero)
    else:
        print("Entrada inválida. Digite um número inteiro válido.")

if lista_numeros:
    lista_primos, lista_nao_primos = separar_primos(lista_numeros)
    print("\nLista original:", lista_numeros)
    print("Números primos:", lista_primos)
    print("Números não primos:", lista_nao_primos)
else:
    print("Nenhum número foi digitado.")


