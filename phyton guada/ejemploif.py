"""realizar un progrma que escriba donde se pida el numero divisor
y el dividendo y arroje si la division es exacta o no
en caso de que no arroje el cociente y el resto"""

Dividendo = int(input("ingrese un número dividendo"))
Divisor = int(input("ingrese un número divisor"))
Cociente = Dividendo // Divisor 
Resto = Dividendo % Divisor

if Resto == 0:
    print("Es una division exacta")
else:
    print("Es una division no exacta",  "el cociente es: " , Cociente, "el resto es" ,Resto)    
      