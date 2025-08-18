# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 07:55:28 2025

@author: casa
"""

class Animal:
    #atributos
    nombre = ""
    tipo_animal = ""
    color = ""
    raza = ""
    collar = False
    
    #metodos, funcionalidades -----> comportamientos
    
    def sonido(self): #self -> objeto perteneciente a la clse
        return "emite sonido"
    def corre(self):
        return "corre"
    def camina (sel):
        return "corre"
    def vuela(self):
        return "vuela"
    def nadar (self):
        return "nada en el agua"
    
    
#%%

# instanciar un objeto

perro = Animal()
perro.nombre = "skyper"
perro.tipo_animal = "canino"
perro.color = "cafe"
perro.raza = "mestizo"
perro.collar = True

print(f"mi primer objeto es {perro.nombre},\n de tipo {perro.tipo_animal},\n de color {perro.color},\n de raza {perro.raza},\n con collar {perro.collar} ")


#%%

class Automovil:
    #atributos   #inicializarlos
    
    #Encapsular -> atributos, metodos __ variables, __ mmetodos 
    def __init__(self):
        self.__largochasis = 2.50
        self.__anchochasis = 1.20
        self.__ruedas = 4
        self.__enmarcha = False
        print("inicializadas las variables")
    
    #metodos
    
    def arrancar (self, arranca):
        self.__enmarcha = arranca
        
        if(self.__enmarcha == True):
            return "el automovil se encuentra en movimiento"
        else:
            return "el automovil esta detenido"
        
    def estado(self):
        print(f"el automovil tiene un largo de chasis {self.__largochasis} m\ncon un ancho de chasis {self.__anchochasis} m\ny tiene {self.__ruedas} ruedas ")
        
        
        #%%
        #
automovil1 = Automovil()
print(automovil1.arrancar(True))
automovil1.estado()


print("--------objeto #2---------")
mustang = Automovil()
print(mustang.arrancar(False))
mustang.estado()

#%%

class Automovil:
    #atributos   #inicializarlos
    
    #Encapsular -> atributos, metodos __ variables, __ mmetodos 
    def __init__(self):
        self.__largochasis = 2.50
        self.__anchochasis = 1.20
        self.__ruedas = 4
        self.__enmarcha = False
        print("inicializadas las variables")
    
    #metodos
    
    def arrancar (self, arranca):
        self.__enmarcha = arranca
        
        if (self.__enmarcha):
            chequeo = self.__chequeoInterno()
        
        if(self.__enmarcha ) and (chequeo):
    
            return "el automovil se encuentra en movimiento"
        elif (self.__enmarcha) and (chequeo == False):
            return "Algo salio mas. EL VEHICULO NO PUEDE ARRANCAR"
        else:
            return "el automovil esta detenido"
        
    def estado(self):
        print(f"el automovil tiene un largo de chasis {self.__largochasis} m\ncon un ancho de chasis {self.__anchochasis} m\ny tiene {self.__ruedas} ruedas ")
    
    #chequear los testigos
    def __chequeoInterno(self):
        print("Realizando chequeo ")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.temperatura = "ok"
        self.puertas = "cerradas"
        if (self.gasolina == "ok") and (self.aceite == "ok") and (self.temperatura == "ok") and (self.puertas == "cerradas"):
            return True
        else :
            return False
        
      #%%
        #
automovil1 = Automovil()
print(automovil1.arrancar(True))
automovil1.estado()


print("--------objeto #2---------")
mustang = Automovil()
print(mustang.arrancar(False))
mustang.estado()


#%%

class estudiante:
    #Encapsular -> atributos, metodos __ variables, __ mmetodos 
    def __init__(self):
        self.__nombre = input("ingrese el nombre del estudiante: ")
        self.__edad = int(input("ingrese la edad del estudiante: "))
        self.__identificacion = int(input("ingrese la identificacion: "))
        print ("estudiante creado")
    def presentacion (self):
        nombre = self.__nombre
        edad = self.__edad
        identificacion = self.__identificacion
        
        print(f"nombre: {self.__nombre}\nedad: {self.__edad}\nIdentificacion: {self.__identificacion}")
        
    def calificacion(self,):
        self.calculo = float(input("ingrese la nota de calculo: "))
        self.humanidades = float(input("ingrese la nota de humanidades: "))
        self.fisica = float(input("ingrese la nota de fisica: "))
        self.estadistica = float(input("ingrese la nota de estadistica: "))
        self.promedio = (self.calculo + self.humanidades + self.fisica + self.estadistica) / 4
        return("sus notas son:\n calculo: {self.calculo}\n humanidades: {self.humanidades}\n fisica: {self.fisica}\n estadistica: {self.estadistica}")
        
    def resumen_final(self,):
        promedio = self.promedio
        if (promedio >= 3):
            print(f"el estudiantes {self.__nombre} APROBO el curso")
        else:
            print(f"el estudiante {self.__nombre} NO APROBO EL CURSO")
            
#%%
estudiante1 = estudiante()
estudiante1.presentacion()
estudiante1.calificacion()
estudiante1.resumen_final()
        