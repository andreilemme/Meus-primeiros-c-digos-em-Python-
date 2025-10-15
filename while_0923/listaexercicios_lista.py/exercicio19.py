nomes = input("Digite uma lista de nomes separados por vírgulas: ").split(",")

nomes_longos = [nome.strip() for nome in nomes if len(nome.strip()) > 5]

print("Nomes com mais de 5 caracteres:", nomes_longos)
