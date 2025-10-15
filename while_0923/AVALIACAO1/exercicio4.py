num = (int)(input("Digite um valor:\n"))
count = 1
if num <= 0:
     print("Valor informado eh negativo e/ou zero")
else:
    while count <= num:
        if num%count == 0:
            print(count)
        count+=1
    