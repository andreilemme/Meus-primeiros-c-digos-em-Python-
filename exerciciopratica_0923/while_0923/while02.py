#Um laço todo pode ser interrompido pelo comando 
#"break. 
#Podemos ainda interromper somente uma passada 
#do laço (iteração) com o comando continue"

numero=0
while numero<10:
    print(numero)
    if numero==5:
      break
    numero+=1
print("saiu do laço com break")

numero=0
while numero<5:
   numero+=1
   print("Pulou o 3...")
   continue
print("fim do laço")

