jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

seleccion = int (input ("Numero del jugador: "))

if seleccion in jugadores:
    print (jugadores[seleccion])
else:
    print ("ESE YA NI JUEGA")
   

