# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 09:39:42 2025

@author: roger
"""

# Super clase - clase padre

class Vehiculo:
    def __init__(self, marca:str, modelo:str):
        self.marca= marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        self.enmarcha = True
        
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
    
    def descripcion (self):
        print(f"marca: {self.marca} \nmodelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelera: {self.acelera} \nFrena: {self.frena}")
        
# Subclase - clase hija

class Moto(Vehiculo):
    acrobacia = ""
    
    def acrobacias (self):
        self.acrobacia = "endo"
    
    def descripcion(self):
        print(f"marca: {self.marca} \nmodelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelera: {self.acelera} \nFrena: {self.frena}\nAcrobacia{self.acrobacia}:")
        
        
# subclase - Clase hija

class Furgoneta(Vehiculo):
     def carga (self, carga):
         self.cargado = carga
         
         if(self.cargado):
             return"la furgoneta esta cargada"
         else:
            return "la furgoneta no esta cargada"
        
class V_electrico(Vehiculo):
    def __init__(self,marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 600
        
    def cargaEnergia(self):
        self.cargado = True

class BiciElectrica: 
    def __init__(self):
        self.autonomia = 60
        
    def cargaEnergia(self):
        self.cargado = True
    
    
class Bici_Electrica(V_electrico,Vehiculo):
    pass

bici_felipe = Bici_Electrica("BMW","Thomson 2024")
bici_felipe.arrancar()
bici_felipe.cargaEnergia()
bici_felipe.descripcion()
    
    
print("_____________________________-")
    
    
    
furgo_will = Furgoneta("polo", "2018")
furgo_will.descripcion()
         
print("--------------------------------------")
moto_roger = Moto("Yamaha","2026 -fz")
moto_roger.arrancar()
moto_roger.acelerar()
moto_roger.descripcion()

#%%

# Super clase - clase padre

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        self.enmarcha = True
        
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
    
    def descripcion (self):
        print(f"marca: {self.marca}, \nmodelo: {self.modelo}, \nEn marcha: {self.enmarcha} \nAcelera: {self.acelera} \nFrena: {self.frena}\nself.acrobacias")
        
# Subclase - clase hija

class Moto(Vehiculo):
    pass 

moto_roger = Moto("Yamaha","2026 -fz")
moto_roger.arrancar()
moto_roger.acelerar()
moto_roger.descripcion()