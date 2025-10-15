#Faça um programa que leia um nome de usuário
#e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro
#e voltando a pedir as informações.
while True:
    nome = input("Informe o nome do usuário")
    senha = input("Informe a senha")
    if(nome==senha):
        print("o nome não pode ser igual a senha")
    else: 
        break
print("SENHA REGISTRADA COM SUCESSO!")
    
