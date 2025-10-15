#Faça um programa que peça uma nota, entre zero
#e dez e exiba a nota digitada.
#Mostre uma mensagem caso o valor seja inválido
#e continue pedindo até que o usuário informe
#um valor válido.
while True:
    fNota = (float)(input("\nDigite uma nota de 0 à 10"))
    if(fNota>=0 and fNota<=10):
        break
    else:
        print("nNota INVÁLIDA!!! Digite novamente")
print( f"\nVocê digitou a nota {fNota}")

