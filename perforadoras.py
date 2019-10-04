"""
Tableta perforadora.
	Basada en la tabla llave códigos perforadora IBM 029
  	La misma contiene 80 columnas y 12 filas
	Posee mayusculas, numeros y caracteres especiales
	Un total de 58 caracteres, (faltan algunos caractes mas)

			TABLA DE LOS CODIGOS DE LOS CARACTERES
			CADA 'X' SIGNIFICA UNA PERFORACION Y ARRIBA EL 
			CARACTER QUE REPRESENTA. 

  /------------------------CARACTERES------------------------\
   0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:@'~“&.<(+|-$*);,%_>?
  ------------------------------------------------------------
12-          XXXXXXXXX                       XXXXXX          -
11-                   XXXXXXXXX                    XXXXX     -
  ------------------------------------------------------------
 0-X                           XXXXXXXXX                XXXXX-
 1- X        X        X        X                             -
 2-  X        X        X        X       X                    -
 3-   X        X        X        X            X     X   X    -
 4-    X        X        X        X      X     X     X   X   -
 5-     X        X        X        X      X     X     X   X  -
 6-      X        X        X        X      X     X     X   X -
 7-       X        X        X        X      X     X         X-
 8-        X        X        X        X XXXXX XXXXX XXXXXXXXX-
 9-         X        X        X        X                     -
  ------------------------------------------------------------

"""

import os
import time

caracter=0
caracteres=[]
columna=["1"]
seleccionado=["|12 |","|11 |","| 0 |","| 1 |","| 2 |","| 3 |","| 4 |","| 5 |","| 6 |","| 7 |","| 8 |","| 9 |"]
valido=True

while True:
	os.system("clear")
	print ("""
--------------------------------------DECODIFICACION---------------------------------------------------		
 _____             _        _               ______             __                        _             
|_   _|           (_)      | |              | ___ \           / _|                      | |            		  
  | |  __ _  _ __  _   ___ | |_  __ _  ___  | |_/ /___  _ __ | |_  ___   _ __  __ _   __| |  __ _  ___        
  | | / _` || '__|| | / _ \| __|/ _` |/ __| |  __// _ \| '__||  _|/ _ \ | '__|/ _` | / _` | / _` |/ __|      
  | || (_| || |   | ||  __/| |_| (_| |\__ \ | |  |  __/| |   | | | (_) || |  | (_| || (_| || (_| |\__ \      
  \_/ \__,_||_|   | | \___| \__|\__,_||___/ \_|   \___||_|   |_|  \___/ |_|   \__,_| \__,_| \__,_||___/      
                 _/ |                                                                                  
----------------|__/-------------------------------------------------------------V0.1---by--pHr4Nt0m---                                                                                   

		""")

	print("Texto      {} " .format(caracteres ))
	print("Columnas   {} \n" .format(columna) )
	print ("-"*102)
	#print ("suma carac ",+caracter)
	print ("""

  -------------------------CARACTERES-------------------------
   0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:@'~“&.<(+|-$*);,%_>?
  ------------------------------------------------------------
12-          XXXXXXXXX                       XXXXXX          -
11-                   XXXXXXXXX                    XXXXX     -
  ------------------------------------------------------------
 0-X                           XXXXXXXXX                XXXXX-
 1- X        X        X        X                             -
 2-  X        X        X        X       X                    -
 3-   X        X        X        X            X     X   X    -
 4-    X        X        X        X      X     X     X   X   -
 5-     X        X        X        X      X     X     X   X  -
 6-      X        X        X        X      X     X     X   X -
 7-       X        X        X        X      X     X         X-
 8-        X        X        X        X XXXXX XXXXX XXXXXXXXX-
 9-         X        X        X        X                     -
  ------------------------------------------------------------
              (Las X indican las perforaciones)

    Indica las filas que deseas marcar para perforar		
Columna ({})  
                            {}     
                            {} 
                            {}
                            {}
                            {}
                            {}
                            {} 
                            {} 
                            {}
                            {}
                            {} 
                            {}   

		""" .format(columna[-1],seleccionado[0],seleccionado[1],seleccionado[2],seleccionado[3],seleccionado[4],seleccionado[5],seleccionado[6],seleccionado[7],seleccionado[8],seleccionado[9],seleccionado[10],seleccionado[11]) )
	print ("""
C  Perforar y pasar a la siguiente columna
D  Desmarcar (Borra todo lo de esta columna)
S  Salir
	""")

	
	

	seleccion= input(": ")

#De acuerdo a valor seleccionado (fila) no da un numero, la suma de estos numeros dan como resutado un caracter
	if seleccion=="S" or seleccion=="s":
		break

	elif seleccion=="12":
		caracter+=100
		seleccionado[0]=" (X)"

	elif seleccion=="11":
		caracter+=200
		seleccionado[1]=" (X)"

	elif seleccion=="0":
		caracter+=400
		seleccionado[2]=" (X)"

	elif seleccion=="1":
		caracter+=1
		seleccionado[3]=" (X)"

	elif seleccion=="2":
		caracter+=2
		seleccionado[4]=" (X)"

	elif seleccion=="3":
		caracter+=3
		seleccionado[5]=" (X)"

	elif seleccion=="4":
		caracter+=4
		seleccionado[6]=" (X)"

	elif seleccion=="5":
		caracter+=5
		seleccionado[7]=" (X)"

	elif seleccion=="6":
		caracter+=6
		seleccionado[8]=" (X)"

	elif seleccion=="7":
		caracter+=7
		seleccionado[9]=" (X)"

	elif seleccion=="8":
		caracter+=8
		seleccionado[10]=" (X)"

	elif seleccion=="9":
		caracter+=9
		seleccionado[11]=" (X)"

# Pone en 0 las variables de los caracteres seleccionados
	elif seleccion=="D" or seleccion=="d":
		caracter=0
		seleccionado=["|12 |","|11 |","| 0 |","| 1 |","| 2 |","| 3 |","| 4 |","| 5 |","| 6 |","| 7 |","| 8 |","| 9 |"]

# suma lo valores de los caracteres seleccionados, si son validos guarda el caracter en la lista caracteres
	elif seleccion=="C" or seleccion=="c": 
		if caracter==400:
			caracteres.append("0")
		elif caracter==1:
			caracteres.append("1")
		elif caracter==2:
			caracteres.append("2")
		elif caracter==3:
			caracteres.append("3")
		elif caracter==4:
			caracteres.append("4")
		elif caracter==5:
			caracteres.append("5")
		elif caracter==6:
			caracteres.append("6")
		elif caracter==7:
			caracteres.append("7")
		elif caracter==8:
			caracteres.append("8")
		elif caracter==9:
			caracteres.append("9")

		elif caracter==101:
			caracteres.append("A")
		elif caracter==102:
			caracteres.append("B")
		elif caracter==103:
			caracteres.append("C")
		elif caracter==104:
			caracteres.append("D")
		elif caracter==105:
			caracteres.append("E")
		elif caracter==106:
			caracteres.append("F")
		elif caracter==107:
			caracteres.append("G")
		elif caracter==108:
			caracteres.append("H")
		elif caracter==109:
			caracteres.append("I")

		elif caracter==201:
			caracteres.append("J")
		elif caracter==202:
			caracteres.append("K")
		elif caracter==203:
			caracteres.append("L")
		elif caracter==204:
			caracteres.append("M")
		elif caracter==205:
			caracteres.append("N")
		elif caracter==206:
			caracteres.append("O")
		elif caracter==207:
			caracteres.append("P")
		elif caracter==208:
			caracteres.append("Q")
		elif caracter==209:
			caracteres.append("R")

		elif caracter==401:
			caracteres.append("/")
		elif caracter==402:
			caracteres.append("S")
		elif caracter==403:
			caracteres.append("T")
		elif caracter==404:
			caracteres.append("U")
		elif caracter==405:
			caracteres.append("V")
		elif caracter==406:
			caracteres.append("W")
		elif caracter==407:
			caracteres.append("X")
		elif caracter==408:
			caracteres.append("Y")
		elif caracter==409:
			caracteres.append("Z")

		elif caracter==10:
			caracteres.append(":")
		elif caracter==12:
			caracteres.append("@")
		elif caracter==13:
			caracteres.append("'")
		elif caracter==14:
			caracteres.append("~")
		elif caracter==15:
			caracteres.append('"')
		elif caracter==100:
			caracteres.append("&")
		elif caracter==111:
			caracteres.append(".")
		elif caracter==112:
			caracteres.append("<")
		elif caracter==113:
			caracteres.append("(")

		elif caracter==114:
			caracteres.append("+")
		elif caracter==115:
			caracteres.append("|")
		elif caracter==200:
			caracteres.append("-")
		elif caracter==211:
			caracteres.append("$")
		elif caracter==212:
			caracteres.append("*")
		elif caracter==213:
			caracteres.append(")")
		elif caracter==214:
			caracteres.append(";")
		elif caracter==411:
			caracteres.append(" ,")
		elif caracter==412:
			caracteres.append("%")

		elif caracter==413:
			caracteres.append("_")
		elif caracter==414:
			caracteres.append(">")
		elif caracter==415:
			caracteres.append("?")
		elif caracter==0:
			caracteres.append(" ")
		else:
			print("Caracteres no validos!!!")
			#columna[-1]-=1
			time.sleep(3)
			valido=False 

		# pone a cero los valores de los caracteres 
		caracter=0
		seleccionado=["|12 |","|11 |","| 0 |","| 1 |","| 2 |","| 3 |","| 4 |","| 5 |","| 6 |","| 7 |","| 8 |","| 9 |"]

		# valida si es correcto el caracter, pasa de columna si no no.
		if valido == True:
			next=int(columna[-1])+1
			columna.append(str(next))






