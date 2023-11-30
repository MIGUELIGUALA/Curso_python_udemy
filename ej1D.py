paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
paises2 = {"Mexico": "CDMX","USA":"Washington DC","Paris":"Francia"}
paises.update (paises2)
seleccion1 = input ("Ingrese un pais: ")

if seleccion1.capitalize () == "Guatemala":
    print (paises["Guatemala"])
elif seleccion1.capitalize () == "El salvador":
    print (paises["El salvador"])
elif seleccion1.capitalize () == "Honduras":
    print (paises["Honduras"])
elif seleccion1.capitalize () == "Nicaragua":
    print (paises["Nicaragua"])
elif seleccion1.capitalize () == "Costa Rica":
    print (paises["Costa Rica"])
elif seleccion1.capitalize () == "Panama":
    print (paises["Panama"])
elif seleccion1.capitalize () == "Argentina":
    print (paises["Argentina"])
elif seleccion1.capitalize () == "Colombia":
    print (paises["Colombia"])
elif seleccion1.capitalize () == "Venezuela":
    print (paises["Venezuela"])
elif seleccion1.capitalize () == "España":
    print (paises["España"])
elif seleccion1.capitalize () == "Mexico":
    print (paises["Mexico"])
elif seleccion1.upper () == "USA":
    print (paises["USA"])
elif seleccion1.capitalize () == "Paris":
    print (paises["Paris"])
else:
    print ("ESE PAIS NO EXISTE EN MI BASE DE DATOS")