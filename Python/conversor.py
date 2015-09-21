#! /usr/bin/ python2
# -*- coding: utf-8 -*-

##############################################
#	Conversor de números a notación IEEE 754 #
##############################################
import sys, os
from argparse import ArgumentParser

num_ingresado = 0
num_binario = ''
parser = ArgumentParser(description='Convierte el número ingresado a la notación IEEE 754.', 
	epilog='<TheMushrr00m | La Espora Del Hongo - 2015>', prog=)
signo = ''

def add_Args():
	""" Añade los argumentos que se pueden pasar a la llamada del programa en la linea de comandos. """
	parser.add_argument('-u', '--url', dest='url', help='URL desde donde comenzar a indexar.', required=True)
	parser.add_argument('-l', '--limite', default=10, dest='limit', help='Limite de URLs a indexar (10 por defecto).', type=int)

def banner():
	print """\033[1;36m
#################################################
#  Conversor de números a notación IEEE 754     #
#  Creado por: Gabriel Cueto Báez               #
#  Ingeniería en Software | Métodos Númericos   #
#################################################	
	
\033[1;32m+ -- -- +=[ Autor: < TheMushrr00m > | Blog: http://laesporadelhongo.com/]
\033[1;33m"""

# Inicia el bucle principal del programa.
if len(sys.argv) == 2:
	# Lee el número pasado como argumento.
	num_ingresado = sys.argv[1]
	convertir_a_binario(num_ingresado)
elif len(sys.argv) <= 2:
	print banner()
else:
	print banner()

def convertir_a_binario(numero):
	bin_Num = ""
	i = 0
	iMask = 1 < 7
	for i in range(1..8):
		if(numero != 0):
			bin_Num += "1"
		else:
			bin_Num += "0"
	pass

