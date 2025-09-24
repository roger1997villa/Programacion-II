# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 09:18:19 2025

@author: casa
"""

import numpy as np

class Matriz_Calificaciones:
    
    #atributo
    
    def __init__(self):
        self.__matriz = []
        
    
     # creacion de la tabla
    def crear_tabla(self,filas, columnas):
          return np.zeros((filas, columnas), dtype=object)
      
    def encabezado(self,tabla):
        for fila in range (1):
            for columna in range(7):
                match columna: 
                    case 0:
                        tabla[fila, columna] = "Estudiante"
                    case 1:
                        tabla[fila, columna] = "calculo"
                    case 2:
                        tabla[fila, columna] = "Español"
                    case 3:
                        tabla[fila, columna] = "Estadistica"
                    case 4:
                        tabla[fila, columna] = "quimica"
                    case 5: 
                        tabla[fila, columna] = "ingles"
                    case 6:
                        tabla [fila, columna] = "sociales"
                    
        return tabla

    def ingresar_valores(self, tabla):
        
        filas, columnas = tabla.shape 
        for i in range(1, filas):              # empieza en 1 para no sobrescribir encabezado
            tabla[i,0] = f"Estudiante {i}"         # nombre de estudiante
            for j in range(1, columnas):
                tabla[i,j] = round(np.random.uniform(0.0,5.0),1) # asignacion de notas de forma aleatoria
        return tabla 
    def mostrar_matriz(self,tabla):
        print("\nMatriz de Calificaciones:\n")
        for fila in tabla:
            for valor in fila:
                print(f"{valor:>12}", end=" ")   # :>12 = ancho fijo, alineado a la derecha
        print()  # salto de línea por cada fila
        
    def promedio_estudiante(self, tabla):
        try:
            i = int(input("Ingrese el número de estudiante que desea saber el promedio: "))
            if i <= 0 or i >= tabla.shape[0]:
                raise IndexError("El numero del estudiante es inválido.")  

            notas = tabla[i, 1:].astype(float)  # todas las notas del estudiante
            promedio = round(notas.mean(), 2) #.mean importado de la libreria numpy prar calcular promedio
            return f"El promedio de {tabla[i, 0]} es {promedio}"

        except (IndexError, ValueError) as e:
            return str(e)
      
    def promedio_general(self, tabla):
        filas, columnas = tabla.shape
        notas = []
        for i in range(1, filas):      # desde 1 porque en la fila 0 está el encabezado
            for j in range(1, columnas): # desde 1 porque en la col 0 está el nombre
                notas.append(float(tabla[i, j]))
        return round(np.mean(notas), 2) 
    
    def nota_maxima(self, tabla):
        filas, columnas = tabla.shape
        max_nota = -1
        estudiante = None
        materia = None

    # recorremos solo las notas (ignorar fila 0 y col 0)
        for i in range(1, filas):
            for j in range(1, columnas):
             nota = float(tabla[i, j])
            if nota > max_nota:
                max_nota = nota
                estudiante = tabla[i, 0]   # nombre estudiante
                materia = tabla[0, j]      # nombre materia

        return f"La nota máxima es {max_nota} en {materia}, obtenida por {estudiante}"
    
      
    
    #%%
    # Crear objeto
mc = Matriz_Calificaciones()

# Crear matriz con 5 filas (1 encabezado + 4 estudiantes) y 7 columnas
tabla = mc.crear_tabla(5, 7)

# Llenar encabezado
tabla = mc.encabezado(tabla)

# Llenar con valores
tabla = mc.ingresar_valores(tabla)

# Mostrar
mc.mostrar_matriz(tabla)


# mostrar promedio del estudiante
print(mc.promedio_estudiante(tabla))


# mostrar promedio general
print("el promedio general es:", mc.promedio_general(tabla))


# mostrar la nota maxima y a quien pertenece
mc.nota_maxima(tabla)