from math import sqrt

A = int (input("Ingresar variable A:"))
B = int (input("Ingresar variable B:"))
C = int (input("Ingresar variable C:"))

x1 = 0
x2 = 0

if ((B**2)-(4*A*C)) < 0:
   print("No se pueden calcular numeros negativos")
else:

 x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
 x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)

 print ("El resultado de \n X1 es :",x1, "El resultado de \n x2 es:",x2)
