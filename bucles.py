print("bucles")
#cuidado con las tabulaciones, el if debe estar tabulado, si no da error

if True:
    print("hola")
    print("hola2")

#variable a=5, comprobar si vale 2, si vale 2, print a=2, si a=5 mostrar a=5
a=5
if (a==2):
    print("a vale 2")
    #este if esta dentro del otro
    if(a<5):
        print("a es menor que 5 dentro del for")  

if(a==2):
    print("a vale 2")
    #este if no esta dentro del otro
if(a==5):
        print("a vale 5 fuera del for")
        
#numero par.
n=10
if n%2==0:
    print("numero par")
else:
    print("numero impar")

comando="otra cosa"

if comando=="entrar":
    print("bienvenido")
elif comando=="saludar":
    print("hola")
elif comando=="salir":
    print("adios")
    
#leer=input
nota=float(input("Introduce una nota. "))
print (nota)

notasejercicio=float(input("Introduce una nota. "))
#elif debe estar a la misma altura del if, el else tambien
if notasejercicio==10:
    print("sobresaliente")
elif notasejercicio>=8 and notasejercicio<10:
    print("notable")
elif notasejercicio<=5 and notasejercicio<8:
    print("bien")
else: print("suspenso")

#bucle while, se pueden anidar los bucles while y for
c=0
while c<=6:
    c+=1
    # aqui se pone , para concadenar
    print("c vale " , c)
    
#bucle for, se puede poner con llaves y f de formato o con coma
for i in range(1,11):
    print(f"tabla del {i}")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    
#preguntar numero y decir la tabla de multiplicar de ese numero usando for
#para pedir un numero, hay que especificarlo, si no por defecto es una cadena

numero=int(input("introduce un numero "))
print("tabla del ",numero)
for i in range(0,11):
    print(numero,"x",i,"=",i*numero)