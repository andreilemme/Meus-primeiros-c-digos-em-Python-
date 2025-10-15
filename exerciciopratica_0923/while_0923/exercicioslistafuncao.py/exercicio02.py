def calcula_volume_esfera(v1):
    pi = 3.14159
    volume = (4/3) * pi * (v1 ** 3)
    return volume

v1 = float(input("Digite o raio da esfera (v1): "))

print(f"O volume da esfera com raio {v1} é {calcula_volume_esfera(v1):.2f}")
