def string_na_lista(string, lista):

    for elemento in lista:
        if string == elemento:
            return True
    return False

minha_string = "banana"
minha_lista = ["maçã", "banana", "laranja"]

print(string_na_lista(minha_string, minha_lista))  

minha_string = "uva"
print(string_na_lista(minha_string, minha_lista))  
