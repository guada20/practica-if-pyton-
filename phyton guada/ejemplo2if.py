"""hacer un programa que pida el nombre , el año que nacio, el año en que estamos
    si año en que estamos es mayor al de nacimiento, arroje la edad de la persona, de lo contrario
    muestre el mensaje el años de nacimiento no puede ser mayor al año actual""" 

Nombre = input("Ingrese su nombre")
AñoNac = int(input("Ingrese el año de nacimiento"))
AñoActual = int(input("Ingrese el año actual"))
Edad = AñoActual - AñoNac
if AñoActual > AñoNac:
    print("su edad es " , Edad)
else:
    print("El año de nacimiento no puede ser mayor al año actual")