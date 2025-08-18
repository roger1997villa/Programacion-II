# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 10:56:24 2025

@author: casa
"""

import script_1 as sl

nombre = input("ingrese un nombre: ")

val1 = int(input("ingrese su primer numero: "))
val2 = int(input("ingrese su segundo numero: "))

sl.saludo()
sl.saludo_predeterminado(nombre)

print("la operacion de la potencia es: ")
print(sl.potencia(val1, val2))
