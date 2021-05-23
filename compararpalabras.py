# programa que solicite dos palabras y muestre cual es mas larga en pantalla
palabra1 = ""
palabra2 = ""
palabra1 = input("sr.usuario ingrese la primera palabra: ")
palabra2 = input("sr.usuario ingrese la segunda palabra: ")
if len(palabra1) > len(palabra2):
    print("sr.usuario la palabra mas larga es: ", palabra1)
elif(len(palabra1) == len(palabra2)):
    print("sr.usuario las palabras son iguales")
else:
    print("sr.usuario la palabra mas lasrga es:", palabra2)
