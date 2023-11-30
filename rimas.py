palabra1 = input ("Ingrese la primera palabra: ")
palabra2 = input ("Ingrese la segunda palabra: ")

if len (palabra1) < 3 or len(palabra2) < 3:
    print ("No rima jaja")
elif palabra1 [-3: ] == palabra2 [-3: ]:
    print ("Estas si son rimas")
elif palabra1 [-2: ] == palabra2 [-2: ]:
    print("Eso rima ahi un 2 2")
elif palabra2 [-10: ] == palabra2 [-10: ]:
    print ("Eso no rima ni un poco")
