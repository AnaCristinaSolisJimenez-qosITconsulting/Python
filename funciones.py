#funciones en python
#las funciones se definen con la palabra clave def
def saludo():
    print("hola, como estas")
    
#llamada de la funcion.
saludo()

def sumar(a,b):
    return a+b

resultado=sumar(3,4)
print("la suma es: ",resultado)

#comprobar numero par con funcion

a=4
def espar(a):
    """ if (a%2==0):
        return True
    else: return False """
#otra forma
    return a%2==0


    
#mandar siempre parametros entre los parentesis
print (espar(a))