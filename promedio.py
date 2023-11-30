P1 = float (input ("Practica No1 :"))
P2 = float (input ("Practica No2 :"))
P3 = float (input ("Practica No3 :"))

P11 = 0

if (P1 + P2 + P3) < 15 :
    print ( " REPROBADO " )
else:
    P11 = (P1 + P2 + P3)/(3)
    print ("El promedio de las practicas es igual a :",P11,)

ExamenP = float (input ("Examen Parcial:"))
ExamenF = float (input ("Examen Final:"))

P12 = 0


if (P11 + ExamenP + ExamenF) < 15 :
    print ( " REPROBADO " )
else:
    P12 = (P11 + 2*ExamenP + 3*ExamenF)/(6)
    print ("El alumno aprobo con:",P12,)


