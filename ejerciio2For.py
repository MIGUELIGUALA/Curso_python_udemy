print ("Ingrese 2 numeros para mostrar el rango entre ellos")
print ("Con numeros pares")
v1 = int (input("Numero 1: "))
v2 = int (input("Numero 2: "))
for i in range (v1,v2+1):
    if i % 2 == 0:
        continue
    print(i)

    