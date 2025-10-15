def eh_multiplo(v1, v2):
    return v1 % v2 == 0

print(eh_multiplo(8, 4))  
print(eh_multiplo(7, 3))  
print(eh_multiplo(5, 5))  

v1 = float(input("Digite o primeiro número (v1): "))
v2 = float(input("Digite o segundo número (v2): "))

print(f"{v1} é múltiplo de {v2}: {eh_multiplo(v1, v2)}")

