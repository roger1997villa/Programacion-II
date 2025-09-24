# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:55:52 2025

@author: casa
"""



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
        
        print(f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nIdentificacion: {self.__identificacion}")
        
    def calificacion(self):
        self.calculo = float(input("ingrese la nota de calculo: "))
        self.humanidades = float(input("ingrese la nota de humanidades: "))
        self.fisica = float(input("ingrese la nota de fisica: "))
        self.estadistica = float(input("ingrese la nota de estadistica: "))
        self.promedio = (self.calculo + self.humanidades + self.fisica + self.estadistica) / 4
        return("sus notas son:\n calculo: {self.calculo}\n humanidades: {self.humanidades}\n fisica: {self.fisica}\n estadistica: {self.estadistica}")
        
    def resumen_final(self):
        promedio = self.promedio
        if (promedio >= 3):
            print(f"el estudiantes {self.__nombre} APROBO EL CURSO con un promedio de: {self.promedio}" )
        else:
            print(f"el estudiante {self.__nombre} NO APROBO EL CURSO con un promedio de: {self.promedio}")
            
#%%
estudiante1 = estudiante()
estudiante1.presentacion()
estudiante1.calificacion()
estudiante1.resumen_final()
        