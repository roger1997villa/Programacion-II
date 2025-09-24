# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 08:37:52 2025
crear una matriz de n*m donde se ingresaran informacion de registros de calificaciones 
unos estudiantes en una determinada materia
@author: roger
"""

import numpy as np
def constructor(estudiantes, notas):
    global calificaciones
    calificaciones = np.full((estudiantes+1, notas+1),None)
    for fila in range(1):
        for columna in range(notas+1):
            if (columna == 0):
                calificaciones [fila,columna]= "Estudiante"
            else : calificaciones[fila, columna] = "nota " + str(columna)
    
def mostrar_matriz():
    return calificaciones
def ingresar_notas():
    for fila in range(1, est+1):
        for columna in range(nots+1):
            if (columna == 0):
                calificaciones[fila,columna] = input("ingrese el nombre del estudiante: ")
            else:
                calificaciones[fila,columna] = input(f"ingrese la nota {columna} del estudiante")


est = int(input("ingrese la cantidad de estudiantes: "))
nots = int(input("ingrese la cantidad de notas: "))
constructor(est, nots)
mostrar_matriz()
ingresar_notas()
    