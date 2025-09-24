# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 09:08:38 2025

@author: casa
"""
class Animal:
    #atributos
    tipo_animal = ""
    color = ""
    raza = ""
    collar = False
    
    # Metodos
    def sonido():
        return sonido
    def corren ():
        return False
    def camina():
        return False
    def vuela():
        return False
    def nada():
        return True
    
    
#Instanciar objeto

perro = Animal()
gato = Animal()
gallo = Animal()
culebra = Animal()
pez = Animal()


perro.tipo_animal = "canino"
perro.color = "cafe"
perro.raza = "salchicha"
perro.collar = True

print(f"Animal: {perro.tipo_animal}")
print(f"Color del animal: {perro.color}")
print(f"Raza: {perro.raza}")
print(f"Collar: {perro.collar}")

