lista = [20, 10,"python", "3.14", 325]

print ("ESTOS SON LOS VALORES ORIGINALES", lista)

palabra1 = input ("Introdusca una palabra: ")
palabra2 = input ("introdusca cualquier otro dato")

lista.insert (0,palabra1)
lista.insert (1,palabra2)

print (lista)
