# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 06:28:11 2025

@author: casa
"""

                
#%%


import numpy as np

 # creacion de la tabla
def crear_tabla(filas, columnas):
    return np.zeros((filas, columnas), dtype=object)

# encabezado de la tabla

def encabezado(tabla):
    for fila in range (1):
        for columna in range(9):
            match columna: 
                case 0:
                    tabla[fila, columna] = "club"
                case 1:
                    tabla[fila, columna] = "PJ"
                case 2:
                    tabla[fila, columna] = "PG"
                case 3:
                    tabla[fila, columna] = "PE"
                case 4:
                    tabla[fila, columna] = "PP"
                case 5:    
                    tabla[fila, columna] = "GF"
                case 6:
                    tabla[fila, columna] = "GC"
                case 7:
                    tabla[fila, columna] = "DG"
                case 8: 
                    tabla[fila, columna] = "Pts"
    return tabla

def llenar_tabla(tabla):
    for fila in range(1, 12):
        tabla[fila, 0] = input("Ingrese el nombre del equipo: ")
        tabla[fila, 2] = int(input("Ingrese la cantidad de partidos ganados: "))
        tabla[fila, 3] = int(input("Ingrese la cantidad de partidos empatados: "))
        tabla[fila, 4] = int(input("Ingrese la cantidad de partidos perdidos: "))
        tabla[fila, 5] = int(input("Ingrese la cantidad de goles a favor: "))
        tabla[fila, 6] = int(input("Ingrese la cantidad de goles en contra: "))
        
        # operaciones
        tabla[fila, 1] = tabla[fila, 2] + tabla[fila, 3] + tabla[fila, 4]  # PJ
        tabla[fila, 7] = tabla[fila, 5] - tabla[fila, 6]                   # DG
        tabla[fila, 8] = tabla[fila, 2] * 3 + tabla[fila, 3]               # Pts
    
    return tabla

def ordenar_tabla(tabla):
    encabezado = tabla[0]  # la primera fila (fila 0)
    datos = tabla[1:]      # las filas de datos (filas 1 a 11)

    # Ordenar los datos por la columna(Pts), de mayor a menor
    datos_ordenados = sorted(datos, key=lambda fila: fila[8], reverse=True)

    # Volver a unir encabezado con datos ordenados
    tabla = np.vstack([encabezado, datos_ordenados])

    return tabla
    

    
                    
                    
                    
                    
#%%


tabla_dim = crear_tabla(11,9)
encabezado(tabla_dim)    
llenar_tabla(tabla_dim)
tabla_dim = ordenar_tabla(tabla_dim)


