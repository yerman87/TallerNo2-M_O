#!/usr/bin/env python
# -*- coding: utf-8 -*

from funciones import *
from metodos_ord import *
import time
import json
import threading

def main():
		b = True
		while b == True:

			menu = ['METODOS DE ORDENAMIENTO', ' \n''1. Insercion ', '2. Por Mezcla', '3. Por Montones (Heap Sort)','4. Rapido (Quicksort)', '5. Por Conteo (Couting Sort)', '6. Por Radix Sort','7. Salir']

			for i in menu:
				print (i)

			p = int(input(" \nSeleccione La opción que desea realizar: "))

			menu1 = ['CANTIDAD DE DATOS', ' \n''1. 1 MILLON ', '2. 2 MILLONES', '3. 5 MILLONES ',
					'4. 10 MILLONES', '5. 20 MILLONES']
			for i in menu1:
				print (i)
			p1 = int(input(" \nSeleccione La cantidad de datos que desea ordenar: "))
			x=cantidad(p1)
			if p ==1:
				tiempo_inicial = time.time()
				lista = crearLista()
				nombre = nombreArchivo()
				llenarLista(lista, x)
				crearCsv(lista, nombre)
				imprimirLista(lista)

				# ordenar
				lista_ordenada = crearLista()
				leerCsv(lista_ordenada, nombre)
				nlista = crearLista()
				nlista2 = arreglalista(lista_ordenada, nlista)
				tam = longitud(nlista2)
				insercionDirecta(nlista2, tam)
				tiempo_inicial_hilo = time.time()
				hilo2 = threading.Thread(target=insercionDirecta, args=(nlista2, tam))
				hilo2.start()
				print ("Lista Ordenada")
				imprimirLista(nlista2)
				nombre_final = nombreArchivo()
				crearCsv(lista_ordenada, nombre_final)
				print ("Tiempo Sin Hilos")
				tiempo_final = time.time() - tiempo_inicial
				imprimirTiempo(tiempo_final)
				print ("Tiempo Con Hilos")
				tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
				imprimirTiempo(tiempo_final_Hilos)

			if p == 2:
				tiempo_inicial = time.time()
				lista = crearLista()
				nombre = nombreArchivo()

				llenarLista(lista, x)
				crearCsv(lista, nombre)
				imprimirLista(lista)
				# ordenar
				lista_ordenada = crearLista()
				leerCsv(lista_ordenada, nombre)
				nlista = crearLista()
				nlista2 = arreglalista(lista_ordenada, nlista)
				tam = longitud(nlista2)
				mergesort(nlista2)
				tiempo_inicial_hilo = time.time()
				#hilo3 = threading.Thread(target=mergesort, args=(nlista2lista))
				#hilo3.start()
				print ("Lista Ordenada")
				imprimirLista(nlista2)
				nombre_final = nombreArchivo()
				crearCsv(lista, nombre_final)
				print ("Tiempo Sin Hilos")
				tiempo_final = time.time() - tiempo_inicial
				imprimirTiempo(tiempo_final)
				print ("Tiempo Con Hilos")
				tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
				imprimirTiempo(tiempo_final_Hilos)


			if p ==3:
				tiempo_inicial = time.time()
				lista = crearLista()
				nombre = nombreArchivo()
				llenarLista(lista, x)
				crearCsv(lista, nombre)
				#imprimirLista(lista)

				# ordenar
				lista_ordenada = crearLista()
				leerCsv(lista_ordenada, nombre)
				nlista = crearLista()
				nlista2 = arreglalista(lista_ordenada, nlista)
				tam = longitud(nlista2)
				heapsort(lista, tam)
				tiempo_inicial_hilo = time.time()
				hilo3 = threading.Thread(target=heapsort, args=(lista, tam))
				hilo3.start()
				print ("Lista Ordenada")
				#imprimirLista(nlista2)
				nombre_final = nombreArchivo()
				crearCsv(lista_ordenada, nombre_final)
				print ("Tiempo Sin Hilos")
				tiempo_final = time.time() - tiempo_inicial
				imprimirTiempo(tiempo_final)
				print ("Tiempo Con Hilos")
				tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
				imprimirTiempo(tiempo_final_Hilos)


			if p ==4:

				tiempo_inicial = time.time()
				lista = crearLista()
				nombre = nombreArchivo()
				llenarLista(lista, x)
				crearCsv(lista, nombre)
				imprimirLista(lista)

				# ordenar
				lista_ordenada = crearLista()
				leerCsv(lista_ordenada, nombre)
				nlista = crearLista()
				nlista2=arreglalista(lista_ordenada,nlista)
				tam = longitud(nlista2)
				quicksort(nlista2, 0, tam -1)
				tiempo_inicial_hilo = time.time()
				hilo1 = threading.Thread(target=quicksort, args=(nlista2, 0, tam -1))
				hilo1.start()
				print ("Lista Ordenada")
				imprimirLista(nlista2)
				nombre_final = nombreArchivo()
				crearCsv(lista_ordenada, nombre_final)
				print ("Tiempo Sin Hilos")
				tiempo_final = time.time() - tiempo_inicial
				imprimirTiempo(tiempo_final)
				print ("Tiempo Con Hilos")
				tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
				imprimirTiempo(tiempo_final_Hilos)

			if p == 5:
				tiempo_inicial = time.time()
				lista = crearLista()
				nombre = nombreArchivo()
				llenarLista(lista, x)
				crearCsv(lista, nombre)
				maximo = max(lista)
				imprimirLista(lista)

				 # ordenar
				lista_ordenada = crearLista()
				leerCsv(lista_ordenada, nombre)
				nlista = crearLista()
				nlista2 = arreglalista(lista_ordenada, nlista)
				tam = longitud(nlista2)
				count_sort(nlista2,maximo)
				tiempo_inicial_hilo = time.time()
				hilo1 = threading.Thread(target=count_sort, args=(nlista2,maximo))
				hilo1.start()
				print ("Lista Ordenada")
				imprimirLista(nlista2)
				nombre_final = nombreArchivo()
				crearCsv(lista_ordenada, nombre_final)
				print ("Tiempo Sin Hilos")
				tiempo_final = time.time() - tiempo_inicial
				imprimirTiempo(tiempo_final)
				print ("Tiempo Con Hilos")
				tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
				imprimirTiempo(tiempo_final_Hilos)

			if p == 6:
				valor = x
				tiempo_inicial = time.time()
				lista = llenar(x)
				nombre = nombreArchivo()
				crearCsv(lista, nombre)
				print ("Lista desordenada")
				imprimirLista(lista)
				# ordenar
				#lista_ordenada = lista
				#leerCsv(lista_ordenada, nombre)
				#nlista = crearLista()
				#nlista2 = arreglalista(lista_ordenada, nlista)
				#tam = longitud(nlista2)
				lista_ordenada=radix_sort(lista)
				tiempo_inicial_hilo = time.time()
				#hilo1 = threading.Thread(target=radix_sort, args=(lista))
				#hilo1.start()
				print ("Lista Ordenada")
				imprimirLista(lista_ordenada)
				nombre_final = nombreArchivo()
				crearCsv(lista_ordenada, nombre_final)
				print ("Tiempo Sin Hilos")
				tiempo_final = time.time() - tiempo_inicial
				imprimirTiempo(tiempo_final)
				print ("Tiempo Con Hilos")
				tiempo_final_Hilos = time.time() - tiempo_inicial_hilo
				imprimirTiempo(tiempo_final_Hilos)
			if p == 7:
				b = False
				print (" Salir del Menu: ")

			if p < 7:
				raw_input("PRESIONE ENTER PARA VOLVER AL MENU:")


if __name__ == '__main__':
      main()