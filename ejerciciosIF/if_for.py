# que pida un numero entero e imprima la palabra hola la cantidad de veces
# segun el numero ingresado si es mayor de cero, o
# de lo contrario decir que el numero es igual a cero o cero
numero = 0
b = "hola"
numero = int(input("sr.usuario ingrese el numero entero: "))
if(numero <= 0):
    print("el valor ingresado es negativo y no se puede imprimir")
else:
    for i in range(0, numero):
        print(b)


