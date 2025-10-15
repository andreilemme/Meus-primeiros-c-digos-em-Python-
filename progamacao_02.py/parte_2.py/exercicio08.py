num = int(input('Digite um número:'))
half_num = num // 2
if num % 2 == 0:
    for exercise_8 in range (1, half_num + 1):
        print(f'{exercise_8}. ',' ' * (exercise_8 - 1),'*' * num, sep='')
    for exercise_8 in range (half_num, 0, - 1):
        print(f'{exercise_8}. ',' ' * (exercise_8 - 1),'*' * num, sep='')
else:
    for exercise_8 in range (1, half_num + 2):
        print(f'{exercise_8}. ',' ' * (exercise_8 - 1),'*' * num, sep='')
    for exercise_8 in range (half_num, 0, - 1):
        print(f'{exercise_8}. ',' ' * (exercise_8 - 1),'*' * num, sep='')