nomes = []
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

maior_nome = max(nomes)
menor_nome = min(nomes)

print("O maior nome em ordem alfabética é:", maior_nome)
print("O menor nome em ordem alfabética é:", menor_nome)
