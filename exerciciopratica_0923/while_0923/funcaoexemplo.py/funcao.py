#|função SEM parâmetro e SEM retorno.
def exibirOi():
    print("Oi")
#função COM parâmetro e SEM retorno
def mostrarMsg(mensagem):
    print(mensagem)
def somar(vr1, vr2):
    print(f"O valor da soma será: {vr1+vr2}")
#Função COM parametro e COM retorno
def multiplicar(vr1,vr2):
    return vr1*vr2
#####################################################
#Caso o parametro linguagem não seja passado, a
#função utilizará como default o Python
def bemvindo(nome,linguagem="Python"):
    print(f"{nome}, seja bem vindo a linguuagem {linguagem}")
#As vezes, é necessário criar uma função com uma
#quantidade de parâmetros indeterminados. Para
#resolver isso, acrescentamos um asterisco antes
#do nome do parâmetro
def exibirNomes(*nomes):
    for nome in nomes:
        print(f"Oi {nome}")
#As vezes é necessário retornar mais de uma informação 



exibirOi()
exibirOi()
mostrarMsg("Olá turma de Si")
somar(15,12)
valor1=10
valor2=55
somar(valor1,valor2)
somar(vr2=7, vr1=9)

mult=multiplicar(3,2)
print(multiplicar(5,8))

bemvindo("Luis")
bemvindo("Alfredo","Assembler")

exibirNomes("Fábio","Carlos","Antonio")