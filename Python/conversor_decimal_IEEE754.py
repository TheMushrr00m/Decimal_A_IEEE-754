#! -*- coding: utf-8 -*-

##############################################
#	Conversor de números a notación IEEE 754 #
##############################################

NEGATIVO = 1
POSITIVO = 0
num_ingresado = 0
num_ingresado_binario = 0
opt_salir = "NO"

def header():
	print """
	#################################################
	#  Conversor de números a notación IEEE 754     #
	#                                               #
	#  Creado por: Gabriel Cueto Báez               #
	#  Blog: http://www.laesporadelhongo.com/       #
	#  GitHub: http://www.github.com/TheMushrr00m/  #
	#  El: 11-Septiembre-2015                       #
	#  Métodos Númericos                            #
	#################################################	
	> Ingresa el número en notación decimal, el cúal, deseas convertir
	  a la notación IEEE-754.\n
	"""

def opt_exit():
	print '¿Desea seguir utilizando el programa?'
	try:
		opt_salir = raw_input('Ingresa SI o NO: ')
		opt_salir = opt_salir.upper()
		if opt_salir == "SI" or opt_salir == "S":
			return False
		elif opt_salir == "NO" or opt_salir == "N":
			print 'Adiós :('
			return True
	except Exception, e:
		print "Ingresa una Opción Valida"

def primer_uso():
	pedir_num()

def pedir_num():
	num_ingresado = input('Ingresa el número a Convertir: ')
	if num_ingresado > 0:
		signo = POSITIVO
	else: 
		signo = NEGATIVO

def convertir_a_binario():
	num_ingresado

header()
pedir_num()
# Initiating the principal bucle of the 'script'.
while not opt_exit():
	pedir_num()

