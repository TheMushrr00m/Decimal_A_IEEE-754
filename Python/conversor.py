#! /usr/bin/ python2
# -*- coding: utf-8 -*-

##############################################
#	Conversor de números a notación IEEE 754 #
##############################################
import sys, os
from argparse import ArgumentParser

args = ''
num_ingresado = 0
num_binario = ''
signo = ''

def banner():
	os.system('clear')
	print """\033[1;36m
#################################################
#  Conversor de números a notación IEEE 754     #
#  Creado por: Gabriel Cueto Báez               #
#  Ingeniería en Software | Métodos Númericos   #
#################################################	
	
\033[1;32m+ -- -- +=[ Autor: < TheMushrr00m > | Blog: http://laesporadelhongo.com/]
\033[1;33m"""

def dec_2_bin(_numero):
	""" Convierte un número decimal a su representación binaria. """
	print "\033[1;36m[*] Comienza la conversión..."
	pass

def float_2_bin(_numero):
	""" Convierte un número con punto decimal a su representación binaria. """
	print "\033[1;36m[*] Comienza la conversión..."
	pass

def leer_numero():
	global num_ingresado
	while True:
		try:
			num_ingresado = input("\033[1;33m[*] Ingresa el número a convertir: ")
			return num_ingresado
		except:
			print "\n\033[1;31m[!] Ingresa un valor númerico...\n"

def main():
	leer_numero()
	if type(num_ingresado) is int:
		dec_2_bin(num_ingresado)
	else:
		float_2_bin(num_ingresado)

if __name__ == '__main__':
	banner()
	main()