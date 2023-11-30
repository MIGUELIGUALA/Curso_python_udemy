entrada = int(input ("Inserte el numero del cual quiera saber el VABS: "))

if entrada > 0:
    print ("El valor absoluto de {} es: {}".format(entrada,entrada))
else:
    print ("El valor absoluto de {} es:".format(entrada),entrada*-1)
