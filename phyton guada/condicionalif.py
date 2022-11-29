"""realizar un programa donde se digite la edad y el nombre
y arroje si la persona es mayor de edad"""

Nombre = input ("ingrese su nombre porfavor")
Edad = int (input("Ingrese la edad"))
if Edad < 18:
    print(Nombre, "Es menor de edad")
else:
    print(Nombre, "Es mayor de edad")     
