num = int(input("Digite um número inteiro: "))

if num < 2:
    print(f"{num} não é primo")
else:
    
    divisor = 2
    primo = True

    while divisor <= num // 2:
        if num % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")
