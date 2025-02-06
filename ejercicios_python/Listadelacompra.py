#### lista de la compra inteligente. En python no hay switch, asi que uso if.
encendido=True
compra=[]

while encendido:
    print ("================================================")
    print ("lista de la compra inteligente")
    print()
    print ("1.añadir un producto a la lista")
    print ("2.eliminar un producto de la lista")
    print ("3.mostrar la lista")
    print ("4.salir de la lista")
    print ("================================================")

    opcion=int(input("elija su opcion "))
    if opcion==1:
        producto=input("¿qué producto desea registrar? ")
        compra+=[producto]
        compra.sort()
        
    elif opcion==2:
        frutaParaBorrar=input("¿qué producto quieres borrar? ")
        if frutaParaBorrar in compra:
            compra.remove(frutaParaBorrar)
            compra.sort()
            print("producto borrado satisfactoriamente")
        else:
            print("ese producto no esta en la lista")

    elif opcion==3:
        for i in compra:
            print(f"-{i}")

    elif opcion==4:
        encendido=False

    else: 
        print("numero no valido")