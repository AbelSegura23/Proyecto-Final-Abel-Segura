from operaciones import operaciones #importacion de la clase operaciones

op = operaciones()

def numeroValido(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.") #Funcion para pedir un numero válido

def menu():
# Función que muestra el menú
    print("-- CALCULADORA -- ")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Cuadrado de un número")
    print("6.- Elevar un numero a otro")
    print("7.- Mostrar el Número Pi")
    print("8.- Mostrar el número e")
    print("9.- Salir")

while True:
    menu()
    elegirOpcion = input("¿Qué operación desea realizar? ")

    if elegirOpcion == '9':
        print("Saliendo de la calculadora")
        break

#Operaciones de Dos números
    if elegirOpcion in ['1', '2', '3', '4']:
        numero1 = numeroValido("Ingrese el Primer Número: ")
        numero2 = numeroValido("Ingrese el Segundo Número: ")

    if elegirOpcion == '1':
        print(f"El resultado es: {op.sumar(numero1, numero2)}")
    
    elif elegirOpcion == '2':
        print(f"El resultado es: {op.restar(numero1, numero2)}")
    
    elif elegirOpcion == '3':
        print(f"El resultado es: {op.multiplicar(numero1, numero2)}")
    
    elif elegirOpcion == '4':
        print(f"El resultado es: {op.dividir(numero1, numero2)}")

 #Operaciones de un solo nú mero   
    elif elegirOpcion == '5':
        numero = numeroValido("Ingrese un Número: ")
        print(f"El resultado es: {op.cuadrado(numero)}")

    elif elegirOpcion == '6':
        base = numeroValido("Ingrese la base: ")
        exponente = numeroValido("Ingrese el exponente: ")
        print(f"El resultado es: {op.potencia(base, exponente)}")  

    elif elegirOpcion == '7':
        print(f"Numero Pi: {operaciones.PI}")

    elif elegirOpcion == '8':
        print(f"Numero e: {operaciones.e}")
        
    else:
        print("Por favor, seleccione una opción del Menú")