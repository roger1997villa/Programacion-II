# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 09:54:09 2025

@author: roger
"""

#Polimorfismo

def suma(a,b):
    return a + b

# 1 Forma

suma(5, 7)

# 2 forma

suma("hola", " a todos")

class coche ():
    def desplzamiento(self):
        print("me desplazo en 4 ruedas")
        
class moto ():
    def desplazamiento(self):
        print("me desplazo en 2 ruedas")
        
class camion ():
    def desplazamiento(self):
        print("me desplazo en 6 ruedas")
        
vehiculo1 = moto()
vehiculo1.desplazamiento()
vehiculo2 = coche()
vehiculo2.desplzamiento()
vehiculo3 = camion()
vehiculo3.desplazamiento()

class Coche:
    def mover(self):
        print("el coche se desplaza por la carretera")
        
class Avion:
    def mover(self):
        print("El avion se desplaza por el aire")
        

def mover_vehiculo(vehiculo):
    vehiculo.mover()
    
renault4 = Coche()
mover_vehiculo(renault4)

