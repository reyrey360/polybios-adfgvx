#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os, argparse
from time import time
import numpy as np
import base64
import hashlib
parser = argparse.ArgumentParser()
# Opciones algoritmos.
parser.add_argument("-polybios", help="Algoritmo de sustitucion monoalfabetica Polybios ", action="store_true")

parser.add_argument("-adfgvx", help="Algoritmo de sustitucion monoalfabetica adfgvx" , action="store_true")

parser.add_argument("-a", help="Despliega ayuda del algoritmo en particular", action="store_true")

parser.add_argument("-cif", help="opcion para cifrar", action="store_true")

parser.add_argument("-c_d", help="opcion para cifrar", action="store_true")

parser.add_argument("-dcif", help="opcion para descifrar", action="store_true")

parser.add_argument("-base64", help="opcion para codificar", action="store_true")

parser.add_argument("-num", help="Si esta activada, el texto se cifra con numeros", action="store_true")

parser.add_argument("-txt", type=str, help="nombre del archivo del texto a cifrar o descifrar", default=os.getcwd(), required=False)

parser.add_argument("-key", type=str, help="clave", default=os.getcwd(), required=False)


args=parser.parse_args()



if args.polybios == True and args.a == True or args.polybios == True and args.cif == False and args.dcif == False:
#if args.polybios == True  or args.polybios == True and args.cif == False and args.dcif == False:


	print("""

		---------------------------UNIVERSIDAD AUTONOMA DE OCCIDENTE--------------------------------
          ---------------------------CERTIFICADO Y FIRMAS DIGITALES-------------------------------

                Sintaxis: ./inicio   <OPCION>                                     
                                                                        
       
           -polybios   :Algoritmo de sustitucion monoalfabetica Polybios

    <OPCION>

    	
    	-polybios 	<Algoritmo de sustitucion monoalfabetica Polybios >


    	-a 			<Despliega ayuda del algoritmo en particular>

    	-cif 		<Opcion para Cifrar>

    	-dcif 		<Opcion para Descifrar>

    	-num        <Cifra con numeros>

    	-txt  		<Nombre del archivo del texto a cifrar o descifrar>



	FORMA DE USO:								  			
								  			
	 Cifrar con numeros:              ./inicio.py  -polybios  -cif  -txt  <nombre_archivo>.txt  -num			
	 Cifrar con letras:               ./inicio.py  -polybios  -cif  -txt  <nombre_archivo>.txt							
     Descifrar:                       ./inicio.py  -polybios  -dcif -txt  <nombre_archivo>.cif   			
     


     INFORMACION: Los archivos  Cifrados se crean en formato   .cif    
        		  Los archivos  Decifrados se crean en formato .dec   
                  Si quiere cifrar un texto que contengas caracteres ascii primero codifiquelo en  base 64
				  Algoritmo muestra el tiempo de ejecucion y el hash asociado al texto a cifrar o decifrar	

	  INGENIERO:.SILER AMADOR DONADO.	

	 ELABORADO POR: 
	 		CRISTIAN M. SANTANDER   reyrey360@gmail.com  codigo 2190535 
			JORGE A. ORTIZ G.  		jorge_alberto.ortiz@uao.edu.co	codigo:2191170	

	---------------------------------------------------------------------------------------------------						  
	
    
        """)



#Cifrado polybios

if args.polybios == True and args.cif == True:
	tiempo_inicial = time()     

#lee el archivo que contiene el mensaje
#ISO 8859-1 es una norma de la ISO que define la codificación del alfabeto latino, 
#incluyendo los diacríticos (como letras acentuadas, ñ, ç), y letras especiales (como ß, Ø), 
#necesarios para la escritura'''

	mensaje=open(args.txt,'r',encoding="ISO-8859-1") 
	mensaje=mensaje.read()
# funcion para guardar el texto cifrado
	cifrar = ""		       

# Cifrado 

	if args.base64 == False:
	
		alfabetot="ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«ÏÙÃÀ][%3_ @@@"

		n = 0
		pos_inicial = -1               # Variable para guardar las posiciones de Ñ y J
		espacios = []                  # cadena donde se guarda todas las posiciones
		lista = ""		       # Variable para guardar la lista de todas las posiciones de Ñ y J separadas por un cero

		pos_inicial1 = -1               # Variable para guardar las posiciones de Ñ y J
		espacios1 = []                  # cadena donde se guarda todas las posiciones
		lista1 = ""		       # Variable para guardar la lista de todas las posiciones de Ñ y J separadas por un cero

#Define el tamaño de la tabla 6x6
		tabla = [[0]*6 for filas in range(7)]  
		for f in range(7):					     # Bucle para cambiar las filas de la tabla de cifrado 
			for c in range(6):			         # Bucle para cambiar las columnas de la tabla de cifrado
				tabla[f][c] = alfabetot[n]	 # Relleno la tabla de cifrado con cada una de las letras del alfabeto
				n += 1

		Mcodificado = mensaje	  


# Cifro el mensaje

		for palabra in Mcodificado:					# Ciclo para recorrer las palabras del mensaje modificado
			for filas in range(0,7):				# Ciclo para recorrer las filas de la tabla de cifrado 
				if palabra in tabla[filas]:			# Condicional para ubicar la fila de la letra a cifrar
					fila = str(filas + 1)			# 1 variable de cifrado
					columna = str((tabla[filas].index(palabra) + 1))	# 2 variable de cifrado
					cifrar += fila + columna


# Calculo del hash

		filename = '/root/Desktop/Criptografia/' + args.txt
		hasher = hashlib.md5()
		with open(filename,"rb") as open_file:
			content = open_file.read()
			hasher.update(content)
		print ("Hash = ", hasher.hexdigest())


# Cifrado con numeros

	if args.num:

		salida = args.txt
		punto = salida.index(".")
		salida = salida[0:punto] + ".cif"
		cripto = open(salida, "w",encoding="ISO-8859-1")
		cripto.write(cifrar)

#Calculo del tiempo total de ejecucion
		tiempo_final = time()			
		tiempo_total = tiempo_final - tiempo_inicial   
		print ("tiempo_total: ", tiempo_total)

# Cifrado con letras
	# Se remplaza los numeros por letras
	else:

		cifrar = cifrar.replace("1","A")			
		cifrar = cifrar.replace("2","B")			
		cifrar = cifrar.replace("3","C")
		cifrar = cifrar.replace("4","D")
		cifrar = cifrar.replace("5","E")
		cifrar = cifrar.replace("6","F")
		cifrar = cifrar.replace("7","G")
		cifrar = cifrar.replace("8","H")
		cifrar = cifrar.replace("9","I")


		#print(len(cifrar))
		#print(len(mensaje))

		salida = args.txt
		punto = salida.index(".")
		salida = salida[0:punto] + ".cif"
		cripto = open(salida, "w", encoding="ISO-8859-1")
		cripto.write(cifrar)

		tiempo_final = time()			       
		tiempo_total = tiempo_final - tiempo_inicial   
		print ("tiempo_total: ", tiempo_total)

# Descifrado polybios

if args.polybios == True and args.dcif == True:

	tiempo_inicial = time()         
# lee archivo cifrado
	cripto=open(args.txt,'r',encoding="ISO-8859-1") 
	cripto=cripto.read()

	cont = 0
	grupo = ""
	desci = ""
	desci_final = ""	       # Vector de string con el mensaje completo 


# Descifro el mensaje
	

	if args.base64 == False:

		alfabetot = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«ÏÙÃÀ][%3_ @@@"
		n = 0
		tabla = [[0]*6 for filas in range(7)]  
		for f in range(7):					  
			for c in range(6):			     
				tabla[f][c] = alfabetot[n]	
				n += 1


	cripto = cripto.replace("A","1")
	cripto = cripto.replace("B","2")
	cripto = cripto.replace("C","3")
	cripto = cripto.replace("D","4")
	cripto = cripto.replace("E","5")
	cripto = cripto.replace("F","6")
	cripto = cripto.replace("G","7")
	cripto = cripto.replace("H","8")
	cripto = cripto.replace("I","9")

	for letras in cripto:
		filas = int(cripto[cont-1])
		columnas = int(cripto[cont])
		cont = cont + 1
		if cont%2 == 0:
			filas = filas - 1
			columnas = columnas -1
			desci = desci + tabla[filas][columnas]

# Decodifico el mensaje
	if args.base64 == True:
		conversion = base64.b64decode(desci)
		decoded = conversion.decode("utf-8")	
	
# Mensaje normal	

	if args.base64 == False:
		decoded = desci

# Guarda el mensaje en texto claro en formato .dec

	salida = args.txt
	punto = salida.index(".")
	salida = salida[0:punto] + ".dec"
	cripto = open(salida, "w", encoding="ISO-8859-1")
	cripto.write(decoded)
	#print(len(desci_final))

# Calculo del hash
	filename = '/root/Desktop/Criptografia/' + salida
	hasher = hashlib.md5()
	with open(filename,"rb") as open_file:
		content = open_file.read()
		hasher.update(content)
	print ("Hash = ", hasher.hexdigest())

	
	tiempo_final = time()			       
	tiempo_total = tiempo_final - tiempo_inicial   
	print ("tiempo_total: ", tiempo_total)

if args.polybios == False and args.cif == False and args.dcif == False and args.adfgvx == False:
	print("""
        -------------------UNIVERSIDAD AUTONOMA DE OCCIDENTE---------------
        ---------------------CERTIFICADO Y FIRMAS DIGITALES----------------

                Sintaxis: ./INICIO <algoritmo>                                        
                                                                        
       
           -polybios   :Algoritmo de sustitucion monoalfabetica Polybios 
           -adfgvx     :Cifrado ADFGVX              
                   
       
	

	  INGENIERO: SILER AMADOR DONADO.	

	 ELABORADO POR: 
	 		CRISTIAN M. SANTANDER   reyrey360@gmail.com  codigo 2190535 
			JORGE A. ORTIZ G.  		jorge_alberto.ortiz@uao.edu.co	codigo:2191170	

		....................................................................						  
	
        """)


if args.adfgvx == True and args.a == True or args.adfgvx == True and args.c_d == False:

	print("""

		---------------------------UNIVERSIDAD AUTONOMA DE OCCIDENTE--------------------------------
          ---------------------------CERTIFICADO Y FIRMAS DIGITALES-------------------------------

                Sintaxis: ./inicio  -adfgvx -cif -dcif -txt <archivo> -key <archivo>                             
                                                                        
       
           -adfgvx   :Cifrado  ADFGVX

                                      <OPCION>

    	
    	-adfgvx 	<Algoritmo de sustitucion monoalfabetica adfgvx >

    	-txt  		<Nombre del archivo del texto a cifrar o descifrar>

    	-a 			<Despliega ayuda del algoritmo en particular>

    	-c_d 		<Opcion para Cifrar y Decifrar el archivo>

    

	FORMA DE USO:								  			
								  			
	 Cifrar y Decifrar u archivo: ./inicio.py  -adfgvx  -c_d  -txt  <nombre_archivo>.txt -key <Archivo con la clave>		
     


     INFORMACION: Los archivos  Cifrados se crean en formato   .cif    
        		  Los archivos  Decifrados se crean en formato .dec   
                  
				

			NOTA: Se recomienda Cifrar y Decifrar archivos pequeños, si son Documentos grandes el proceso sera largo.		

	  		INGENIERO:.SILER AMADOR DONADO.	

	 ELABORADO POR: 
	 		CRISTIAN M. SANTANDER   reyrey360@gmail.com codigo 2190535	  
			JORGE A. ORTIZ G.  		jorge_alberto.ortiz@uao.edu.co	codigo :2191170		

	---------------------------------------------------------------------------------------------------						  
	
    
        """)


	

if args.adfgvx == True and args.c_d == True:
	
	tiempo_inicial = time()    



	#f1 = open ("claro.txt")
	#text = f1.read()

	# En la clave no deben estar los mismos caracteres!

	#f = open ("key.txt")
	#key = f.read()

	text=open(args.txt,'r', encoding="ISO-8859-1")
	text=text.read()

	key=open(args.key,'r')
	key=key.read()

	# Llaves de repuesto
	keys = {
		'A':'AA', 'B':'AD', 'C':'AF', 'D':'AG', 'E':'AV', 'F':'AX',
		'G':'DA', 'H':'DD', 'I':'DF', 'J':'DG', 'K':'DV', 'L':'DX',
		'M':'FA', 'N':'FD', 'O':'FF', 'P':'FG', 'Q':'FV', 'R':'FX',
		'S':'GA', 'T':'GD',	'U':'GF', 'V':'GG', 'W':'GV', 'X':'GX',
		'Y':'VA', 'Z':'VD', '1':'VF', '2':'VG', '3':'VV', '4':'VX',	
		'5':'XA', '6':'XD', '7':'XF', '8':'XG', '9':'XV', '0':'XX'
		
	}


	# <-- Cifrado --> #

	### Primera etapa ###
	# Método de cifrado de 
	encryptOne = []
	for i in text:
		if i in keys:
			encryptOne.append(keys[i])
	#print(encryptOne)

	### Segunda etapa ###
	# Separa todos los letras uno por uno
	length = len(encryptOne)
	for i in range(length):
		for j in range(2):
			encryptOne.append(encryptOne[i][j])
	for i in range(length):
		encryptOne.remove(encryptOne[0])
	#print(encryptOne)

	# Si bien el mensaje cifrado no está dividido 
	# por la longitud de la clave, agregue caracteres dobles

	while len(encryptOne)%len(key) != 0:
		element = 'XV'
		for i in range(2):
			encryptOne.append(element[i])
	#print(encryptOne)

	# Permutación de la clave alfa

	listKey = [x for x in key]
	#print(listKey)
	# Tecla después de permutación alfabéticamente
	listKey.sort()
	#print(listKey)
	#print()

	# Creación de listas anidadas 
	# basadas en la longitud del mensaje cifrado
	listSort = []
	length = len(encryptOne)/len(key)
	for i in range(int(length)):
		listSort.append([])
	#print()

	# Dividiendo una lista en muchas
	#  listas anidadas
	k = 0
	for i in range(len(encryptOne)):
		if i == 0 or i%len(key) != 0:
			listSort[k].append(encryptOne[i])
		else:
			k += 1; listSort[k].append(encryptOne[i])
	for i in listSort:
		i
		#print(i)
	#print()

	# Sustitución de cada personaje clave
	# por k caracteres de su índice
	dictKey = {x:[] for x in key}
	for i,j in enumerate(dictKey):
		for n in range(len(listSort)):
			dictKey[j].append(listSort[n][i])
	for i in dictKey:
		i
		#print(i,dictKey[i])
	#print()

	# Permutación de teclas alfabética
	encryptTwo = []
	for i in listKey:
		for j in dictKey:
			if i == j:
				encryptTwo.append(dictKey[j])
	#			print(j,dictKey[j])
	#print()

	# Mensaje cifrado
	encrypt = ""
	for x in range(len(encryptTwo)):
		for y in range(len(encryptTwo[x])):
			encrypt += encryptTwo[x][y]
	#print("Mensaje Encriptado :",encrypt,"\n")



	#encry = open('claro.cif','w' )
	#encry.write ((str(encrypt)))
	#encry.close()

	# Guarda el mensaje en texto claro en formato .dcif

	salida = args.txt
	punto = salida.index(".")
	salida = salida[0:punto] + ".cif"
	cripto = open(salida, "w", encoding="ISO-8859-1")
	cripto.write(encrypt)


	#####
	# <-- Descifrado --> #
	
	# Mensaje cifrado y clave
	encrypt = encrypt
	key = key
	keys = keys

	# Llave original
	key1 = [x for x in key]
	#print(key1)


	# Reorganizar la clave en orden alfabético.
	key2 = [x for x in key1]
	key2.sort()
	#print(key2)
	#print()

	# Calcular el número de listas anidadas
	length = len(encrypt)/len(key1)

	# Agregar una cierta cantidad a la lista
	# listas anidadas
	arr = []
	for i in range(int(length)):
		arr.append([])

	# Adición y distribución letra por carácter de un mensaje
	# cifrado a las celdas de la lista
	for i in range(len(encrypt)):
		for l in range(int(length)):
			if i%int(length) == l:
				arr[l].append(encrypt[i])
	for i in arr:
		#print(i)
		i
	#print()

	# Enumerar todos los símbolos clave y
	# asignar una lista a cada símbolo
	dictKey = {x:[] for x in key2}

	# Agregue el valor de los caracteres del mensaje cifrado
	# a cada símbolo de clave
	for i,j in enumerate(dictKey):
		for n in range(len(arr)):
			dictKey[j].append(arr[n][i])
	for i in dictKey:
		#print(i,dictKey[i])
		i,dictKey[i]
	#print()

	# Caracteres de distribución clave
	# En el orden original
	decryptTwo = []
	for i in key1:
		for j in dictKey:
			if i == j:
				decryptTwo.append(dictKey[j])
	for i in range(len(decryptTwo)):
		#print(key1[i],decryptTwo[i])
		key1[i],decryptTwo[i]
	#print()

	# Creando una lista con listas anidadas
	listSort = []
	for i in range(int(length)):
		listSort.append([])

	#  Enumerar la lista decryptTwo e 
	# ingresar los valores de encryptString a
	# listSort en orden de índices
	encryptString = ""
	for i in range(len(decryptTwo)):
		for j in range(len(decryptTwo[i])):
			encryptString += decryptTwo[i][j]
	for i in range(len(encryptString)):
		for l in range(int(length)):
			if i%int(length) == l:
				listSort[l].append(encryptString[i])
	for i in listSort:
		# print(i)
		i
	#print()

	# Agregar a la lista decryptOne todos
	# los caracteres de la listSort
	decryptOne = []
	for x in range(len(listSort)):
		for y in range(len(listSort[x])):
			decryptOne.append(listSort[x][y]) 
	#print(decryptOne)

	# Creando pares de personajes
	for i in range(0,len(decryptOne)):
		if i%2 == 0:
			decryptOne[i] = decryptOne[i] + decryptOne[i+1]
	for i in decryptOne:
		if len(i) == 1:
			decryptOne.remove(i)
	#print(decryptOne)

	# Descifrado de un mensaje de par cifrado por claves
	decrypt = ""
	for i in range(len(decryptOne)):
		for j in keys:
			if decryptOne[i] == keys[j]:
				decrypt += j

	#print("\n Mensaje desencriptado :",decrypt)

	#archivo = open('claro.dec','w' )
	#archivo.write ((str(decrypt)))
	#archivo.close()

		# Guarda el mensaje en texto claro en formato .dec

	salida = args.txt
	punto = salida.index(".")
	salida = salida[0:punto] + ".dec"
	cripto = open(salida, "w", encoding="ISO-8859-1")
	cripto.write(decrypt)





