num = int(input("Digite um número: "))
for linha in range (1, num + 1):
    print(f'{linha}. ','_' * (num - linha),'*','_*' * (linha - 1), sep='')