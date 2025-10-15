numBig = -1
while True:
    num = (int)(input("Digite um valor:\n"))
    if num < 0 :
        break
    if numBig < num:
        numBig = num
print(numBig)