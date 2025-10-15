#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#idade: entre 0 a 150;
#Salário: maior que zero;
#Gênero: 'f' ou 'm';
#Estado Civil 

# Função para validar nome
def validar_nome(nome):
    return len(nome) > 3

# Função para validar idade
def validar_idade(idade):
    return 0 <= idade <= 150

# Função para validar salário
def validar_salario(salario):
    return salario > 0

# Função para validar gênero
def validar_genero(genero):
    return genero in ['f', 'm']

# Função para validar estado civil
def validar_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']  # Solteiro, Casado, Viúvo, Divorciado

# Loop para coletar e validar as informações
def coletar_informacoes():
    while True:
        nome = input("Digite o nome (maior que 3 caracteres): ")
        if validar_nome(nome):
            break
        print("Nome inválido. Tente novamente.")

    while True:
        try:
            idade = int(input("Digite a idade (entre 0 e 150): "))
            if validar_idade(idade):
                break
            else:
                print("Idade inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    while True:
        try:
            salario = float(input("Digite o salário (maior que zero): "))
            if validar_salario(salario):
                break
            else:
                print("Salário inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    while True:
        genero = input("Digite o gênero ('f' para feminino, 'm' para masculino): ").lower()
        if validar_genero(genero):
            break
        print("Gênero inválido. Tente novamente.")

    while True:
        estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()
        if validar_estado_civil(estado_civil):
            break
        print("Estado civil inválido. Tente novamente.")

    print("\nInformações válidas coletadas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Gênero: {'Feminino' if genero == 'f' else 'Masculino'}")
    print(f"Estado Civil: {estado_civil}")

# Executar o programa
coletar_informacoes()


