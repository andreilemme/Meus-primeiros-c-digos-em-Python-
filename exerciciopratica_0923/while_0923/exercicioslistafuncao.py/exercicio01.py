def maior_numero(v1, v2):
    return v1 if v1 > v2 else v2

v1 = float(input("Digite o primeiro número (v1): "))
v2 = float(input("Digite o segundo número (v2): "))

print(f"O maior número entre {v1} e {v2} é {maior_numero(v1, v2)}")
