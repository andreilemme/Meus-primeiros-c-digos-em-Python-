alunos=[]
qtde = (int)(input("Informe a quantidade de alunos: "))
for i in range(0,qtde):
    nome = input(f"Digite o nome do {i+1} aluno: ")
    alunos.append(nome)
#Apagando um elemento
del alunos[2]
alunos.pop(0)

for i in range(0,len(alunos)):
    print(f"{i+1}aluno: {alunos[i]}")
