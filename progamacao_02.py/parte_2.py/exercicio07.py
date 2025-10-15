num = int(input('Digite um número:'))
if num % 2 == 0:
    for linha in range (1, num + 1):
        print(f'{linha}. ',' ' * (linha - 1),'*', sep='')
    for linha in range (num, 0, - 1):
        print(f'{linha}. ',' ' * (linha - 1),'*', sep='')
else:
    for linha in range (1, num + 2):
        print(f'{linha}. ',' ' * (linha - 1),'*', sep='')
    for linha in range (num, 0, - 1):
        print(f'{linha}. ',' ' * (linha - 1),'*', sep='')