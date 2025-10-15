import bcrypt

# Função para criptografar a senha usando bcrypt
def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt)

# Função para verificar a senha
def verificar_senha(senha, senha_armazenada):
    return bcrypt.checkpw(senha.encode(), senha_armazenada)

# Função para registrar um novo usuário
def registrar_usuario():
    usuario = input("Crie um nome de usuário: ")
    senha = input("Crie uma senha forte: ")
    senha_criptografada = criptografar_senha(senha)
    
    # Salva o usuário e a senha criptografada em um arquivo (simulando um banco de dados)
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario}:{senha_criptografada.decode()}\n")
    print("Usuário registrado com sucesso!")

# Função para fazer login
def fazer_login():
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    # Verifica se o usuário e a senha correspondem
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            user, senha_salva = linha.strip().split(":")
            if user == usuario and verificar_senha(senha, senha_salva.encode()):
                print("Login bem-sucedido! Bem-vindo,", usuario)
                return
    print("Usuário ou senha incorretos.")

# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Autenticação ---")
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            fazer_login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
