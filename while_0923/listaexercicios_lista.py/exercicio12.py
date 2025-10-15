frase = input("Digite uma frase: ")

if frase.strip():
    palavras = frase.split()
    
    print("Lista de palavras:", palavras)
    
    frase_invertida = []
    i = len(palavras) - 1
    while i >= 0:
        frase_invertida.append(palavras[i])
        i -= 1
    
    frase_invertida_str = " ".join(frase_invertida)
    print("Frase na ordem inversa:", frase_invertida_str)
else:
    print("Nenhuma frase foi digitada.")




#Daqui em diante ChaGPT está me ajudando 100% (Antes era 50%. Se sinceridade valer ponto eu fico grato :) Brincadeira poh.
