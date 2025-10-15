def verifica_numero(numero):
    if numero > 0:
        print("POSITIVO")
    elif numero < 0:
        print("NEGATIVO")
    else:
        print("NULO")

num = float(input("Digite um número: "))

verifica_numero(num)
