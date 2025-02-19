numeros="9";
x=input("indica cuantas lineas debe tener: ")
i=0
for i in range(0, int(x), 1):
    print(" "*(int(x)-i-1)+numeros)
    numeros+="99"