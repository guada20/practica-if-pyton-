"""realizar un programa que pida edad y grupo (adultos, infante)
si la edad es mayor o igual a 18 y grupo escogido igual adultos debe mostrar Puedes entrar, si edad menor que 18 
y grupo adultos muestre
No puedes ingresar al grupo eres menor de 18
si edad menor que 18 si edad menor que 18 y grupo infantes muestre 
puedes ingresar cumple con las condiciones
de lo contrario muestre Esta opcion no es valida"""

Edad = int(input("ingrese su edad"))
Grupo = input("ingrese su grpo: adultos o infante")

if Edad >= 18 and Grupo == "adultos": 
    print("Puedes entrar")
elif Edad < 18 and Grupo == "adultos":
    print("No puedes ingresar al grupo eres menor de 18")
elif Edad < 18 and Grupo == "infante":
    print("puedes ingresar cumples con las condiciones")
else:
    print("Esta opcion no es valida")
