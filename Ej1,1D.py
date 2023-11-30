paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
          "Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
          "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
datos = input("Ingrese un pais para saber su capital: ")

metodo = datos.capitalize () in paises

if metodo:
    print (paises [datos.capitalize()])
else:
    print ("NOSTA")
