print(3+2)
n=4
print(n)
nota1=2
nota2=5
notaMedia=(nota1+nota2)
print(notaMedia)
#cadenas, las cadenas se pueden poner entre comillas simples o dobles
'hola mundo'
"hola mundo"
"Esta \"palabra\" va entre comillas"
print("Esta \"palabra\" va entre comillas")
print("una linea \notra linea")
cadena="hola"
print(cadena*2)

espacios=" "
#se concadena con +
print("estos son 10 espacios: "+ espacios*10+".")

palabra="Python"

#como los arrays, posicion de [1] para sacar la y
print(palabra[1])

#da la vuelta a la cadena y saca el ultimo caracter
print(palabra[-1])

#desde posicion 1 a posicion 2, la 0 no se incluye.
print(palabra[0:2])

# en pyton las cadenas son inmutables
#no se puede poner palabra[0]=n

#listas pueden ser de numeros, cadenas, reales etc y se pueden mesclar los datos
numeros=[1,2,3,4,5]
print(numeros)

datos=[1,'esto es una cadena',2.4]
#datos
print(datos)
#cuidado con "1" y 1, uno es cadena y el otro numero
#len=longitud de lista
print(len(datos))

#ultimo digito
#muestra los datos de longitud de datos -1
print(datos[len(datos)-1])

datos[-7:-1]
numeros=[1,2,3,5]
numeros + [6,7,8,9]
print (numeros + [6,7,8,9])

pares=[2,4,5,8,10]
print(pares)

#se puede sobreescribir, las cadenas no, las listas si
pares[2]=6
print(pares)

letras=('a','b','c','d','e','f')
print(letras)

print(letras[0:3])
 
print(letras[:3])

letras[:3]=['A','B','C']
print (letras)
#pasar las letras  a mayuscula
print(letras)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

r=[a,b,c]

print(r)
print("====================")
print(r[1])
print(r[1][1])
print(r[-1])
print(r[-1][-1])

print(1+1==3)

print()

print(1+1==2)
#mismos operadores logicos que java y se pueden mezclar con multiplicaciones
#para cadenas se pueden usar los operadores logicos en lugar de equals
print("hola"=="hola")
l1=[0,1,2]
l2=[0,1,4]
print(l1==l2)
print(len(l1)==len(l2))

#se puede usar not true, true and true, false and true, false or true

c="Hola mundo"
print(len(c)>=20 and c[0]=="H")
print("==================")
# es sensible a mayúsculas
print(len(c)>=20 or c[0]=="H")

c="lectura"

print(c[0]=="H"or c[0]=="h")

a=5
a=a+2
print(a)
a+=3
print(a)

print("========================")
