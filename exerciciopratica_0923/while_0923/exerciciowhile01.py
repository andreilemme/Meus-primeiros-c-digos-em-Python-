#Crie um programa que leia diversas notas de alunos
#e exiba a quantidade de alunos e a média das notas.
#Para encerrar a entrada das notas, digite -1.
somaNotas = 0
contarNotas = 0
while True:
    nota = (float)(input(
     "Informe a nota. (-1 para encerrar): "))
    if nota==-1:
        break
    somaNotas+=nota
    contarNotas+=1
    media = somaNotas/contarNotas
    #.2f colocará duas casas decimais no número
    print(f"Quantidade de notas: {contarNotas}\nMédia: {media:.2}")
else:
    print("Nenhuma nota foi registrada")
    
