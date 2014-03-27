#!/usr/bin/python
#!encoding: UTF-8

print " Introduzca el nombre del fichero donde se encuentran los resultados: "
nombre_fich=raw_input()
try:
  fichero=open(nombre_fich)
  linea=fichero.readline()
  while(linea != ""):
    aprox = int(linea.split()[3])
    print(" Nº de intervalos: %d" % (aprox))
    for i in range (5):
      linea=fichero.readline()
      porcentaje=linea.split()[0]
      umbral=float(linea.split()[6])
      print(" %s de fallos para el umbral %2.5f" % (porcentaje, umbral))
    linea=fichero.readline()
except:
  print " El nombre del fichero introducido es incorrecto"