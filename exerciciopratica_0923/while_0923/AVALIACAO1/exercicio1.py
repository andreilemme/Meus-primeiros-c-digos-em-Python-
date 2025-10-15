num = (int)(input("Digite um valor inteiro positivo:\n" ))
count= 0 
sum = 0
if num > 0:
    while (count <= num):
        sum = sum + count
        count +=1
    print(f"A soma de 1 a {num} eh {sum}")
else:
    print("Valor informado eh negativo e/ou zero")

#ou pode fazer desse jeito:
numero = (int)(input("Digite um número inteiro positivo"))
soma = 0
for i in range(1,nuumero+1):
    soma+= #soma=soma+i
print(f"A soma de 1 até {numero} será {soma}")