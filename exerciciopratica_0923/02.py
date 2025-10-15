# Número predefinido para calcular o fatorial
num = 5  # Você pode mudar esse valor para outro número

# Inicializa a variável para armazenar o fatorial
fatorial = 1

# Loop para calcular o fatorial de num
for i in range(1, num + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {num} é: {fatorial}")

#Explicação mais detalhada:
#Definindo o número: No código, o valor num = 5 está predefinido para calcular o fatorial de 5. Você pode mudar esse número para qualquer outro inteiro.
#Cálculo do fatorial: O loop for vai multiplicando os valores de 1 até num. Por exemplo, se num = 5, o loop vai calcular: 1 * 2 * 3 * 4 * 5.
#Resultado: O resultado do fatorial é armazenado na variável fatorial e exibido ao final.