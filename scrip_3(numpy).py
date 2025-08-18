# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 12:16:56 2025

@author: casa
"""

import numpy as np
print(np.pi)
print(np.e)


vector1= [5, 6, 8]
vector2 = np.array([5, 6, 8])
vector3 = np.array([[5, 7, 8, 4],
                    [3, 2, 1, 0]])

print(f"dimension {vector2.shape}")
print(f"cantidad de dimensiones{vector2.ndim}")

print(vector3, end=" ")

iteracion = 0
for fila  in vector3:
    iteracion += 1
    print(f"{iteracion}:{fila}")
    
    
for fila in vector3:
    for elemento in fila:
        print(elemento)
    
    
   
for fila in vector3:
    for elemento in fila:
        print(elemento, end=" ")
    print()
    
vector4 = np.array([[5, 7, 8.3, 4],
                    [3, 2, 1, 0]])
  
for fila in vector4:
    for elemento in fila:
        print(elemento, end=" ")
    print()
    
type(vector3[1][2])
type(vector4[1][2])

vector5 = np.zeros((3,3))
vector6 = np.ones((3,3))
vector7 = np.eye(5)
vector8 = np.full((11, 9), None)
vector9 = np.random.rand(4,2)
vector10 = np.random.randint(0,2,(8,3))
vector11 = np.identity(5)
vector12 = np.arange(1,11,2)
vector13 = np.linspace(1,25,30)
