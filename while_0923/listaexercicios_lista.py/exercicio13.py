idades = [12, 25, 17, 34, 15, 40, 19, 16, 22, 18]

media_idade = sum(idades) / len(idades)

maiores_18 = sum(1 for idade in idades if idade > 18)
menores_18 = sum(1 for idade in idades if idade < 18)

print("A idade média do grupo é:", media_idade)
print("Número de pessoas maiores de 18 anos:", maiores_18)
print("Número de pessoas menores de 18 anos:", menores_18)
