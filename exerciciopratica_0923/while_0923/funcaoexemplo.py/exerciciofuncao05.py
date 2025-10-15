#Elabore um programa em Python, onde o usuário
#digitará uma senha e em seguida repetirá a 
#digitação. Crie uma função que receberá como 
#parâmetro as duas senhas e retornará se elas 
#são iguais ou não. Exiba a resposta.
def verificar(password,repeat):



senha = input("Digite a senha: ")
repete = input("Digite novamente a senha: ")

# Função que verifica se duas senhas são iguais
def verifica_senhas(senha1, senha2):
    if senha1 == senha2:
        return "As senhas são iguais."
    else:
        return "As senhas são diferentes."

# Solicita a senha do usuário duas vezes
senha1 = input("Digite sua senha: ")
senha2 = input("Repita sua senha: ")

# Chama a função para verificar as senhas e exibe a resposta
resultado = verifica_senhas(senha1, senha2)
print(resultado)
