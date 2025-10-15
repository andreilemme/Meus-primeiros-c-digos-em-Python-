num = int(input("Digite um número: "))
for linha in range(num, 0, -1):
    print(f'{linha}. ', '_' * (num - linha), '*', '_*' * (linha - 1), sep='')