num = int(input("Digite um número: "))
for linha in range (1, num + 1):
    print(f'{linha}. ',' ' * (linha - 1),'*' * num, sep='')