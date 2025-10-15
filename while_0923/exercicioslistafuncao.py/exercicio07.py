def validar_string(string, min_caracteres, max_caracteres):
    tamanho = len(string)
    
    
    if min_caracteres <= tamanho <= max_caracteres:
        return True
    else:
        return False


string1 = "Exemplo"
min_caracteres = 3
max_caracteres = 10

print(validar_string(string1, min_caracteres, max_caracteres))  

string2 = "Texto muito longo"
print(validar_string(string2, min_caracteres, max_caracteres))  