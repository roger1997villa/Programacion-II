# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 07:20:50 2025

@author: casa
"""

import numpy as np

def crear_tabla():
    filas = int(input("ingrese el numero de filas: "))
    columnas = int(input("ingrese el numero de columnas: "))
    return np.zeros((filas, columnas), dtype=int)

def organizar_tabla(tabla):
    filas, columnas = tabla.shape
    
    for i in range(filas):
        for j in range(columnas):
            tabla[i, j] =  (i + j) %2
    return tabla
    

    
tabla = crear_tabla()

tabla = organizar_tabla(tabla)

print(tabla)