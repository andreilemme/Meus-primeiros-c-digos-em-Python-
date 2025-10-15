#Faça um programa, utilizando while, que permita ao
#usuário realizar a soma de 2 números. Ele poderá
#fazer quantas contas quiser. Pergunte ao usuário
#se ele deseja fazer nova soma ou não.
while True: 
    Num1 = (int)(input("digite aqui"))
    Num2 = (int)(input("digite aqui"))
    soma = Num1+Num2
    print(soma) 
    resposta = (input("Deseja continuar a soma?"))
    if(resposta== "N"): 
        break
    
