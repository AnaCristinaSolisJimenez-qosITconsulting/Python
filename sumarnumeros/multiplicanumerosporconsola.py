def mostrar_multiplicacion_vertical(numero1, numero2):
    """
    Esta función muestra la multiplicación de dos números de forma vertical,
    simulando el procedimiento que se realiza en papel.
    
    Args:
    numero1 (int): Primer número a multiplicar.
    numero2 (int): Segundo número a multiplicar.
    """
    num1 = str(numero1)
    num2 = str(numero2)
    resultado = numero1 * numero2
    
    # Imprime los números alineados para la operación
    print(f"  {num1}")
    print(f"× {num2}")
    print("-" * (max(len(num1), len(num2)) + 2))
    
    # Inicializa el número de espacios para alinear los productos parciales
    espacios = len(num2) - 1
    
    # Itera sobre cada dígito del segundo número, multiplicándolo por el primero
    for i, digito in enumerate(reversed(num2)):
        parcial = numero1 * int(digito)  # Calcula el producto parcial
        print(" " * espacios + str(parcial))  # Ajusta los espacios para alinear la salida
        espacios -= 1  # Reduce los espacios en cada iteración
    
    # Imprime la línea separadora y el resultado final
    print("-" * (len(str(resultado)) + 2))
    print(f"  {resultado}")

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
mostrar_multiplicacion_vertical(num1, num2)
