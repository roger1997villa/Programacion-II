# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 07:19:51 2025

@author: roger
"""

class Banco:
    nombre = ""
    def __init__(self, nombreBanco):
        self.nombre = nombreBanco
class Empleado:
    nombre = ""
    def __init__(self,nombreEmpleado):
        self.nombre = nombreEmpleado
        
Bancolombia = Banco("Bancolombia")
Nicolas = Empleado("Nicolas Cortes")

print(f"El sr {Nicolas.nombre}, tiene cuenta en el banco {Bancolombia.nombre}")        
    
#%%
# Relacion de 

class Colegio:
    nombre = ""
    ubicacion = ""
    
    
    def __init__(self,nombreCol,ubicacionCol):
        self.nombre = nombreCol
        self.ubicacion = ubicacionCol
        self.estudiantes = []
    
    
    def adicionar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
        
    def eliminar_estudiante(self,estudiante):
        for e in self.estudiantes:
            if (e == estudiante):
                self.estudiantes.remove(estudiante)
    
    def mostrar_estudiantes(self):
       print("Los estudiantes son: ")
       for estudiante in self.estudiantes:
           print(estudiante)
    
    
class Estudiante:
     def __init__(self,nombreEstudiante,edadEstudiante,gradoEstudiante):
         self.nombre: str = nombreEstudiante
         self.edad: int= edadEstudiante
         self.grado: str = gradoEstudiante
         self.promedio: float = 0.0
         
     def __str__(self):
         return  f"{self.nombre}, {self.edad}, {self.grado}, {self.promedio}"
    
     def promedio(self,notas):
         suma = 0 
         for i in notas:
             self.suma += i
         self.promedio = self.suma / len(notas)
     def informacion_estudiante(self):
         print(f"El estudiante es {self.nombre} con edad {self.edad}, del grado {self.grado} tiene es siguiente promedio: {self.promedio}")
        
     
         
        
san_pablo = Colegio("San Pablo", "Victoria-Caldas")
e1 = Estudiante("Roger Villa", 27,"pregrado")
e2 = Estudiante("Wilfredo Calderon", 21,"pregrado")
e3 = Estudiante("Nicolas Cortes", 18,"pregrado") 
e4 = Estudiante("Felipe Choconta", 21,"pregrado")
e5 = Estudiante("Miller Quiroga", 45,"pregrado")
san_pablo.adicionar_estudiante(e1)
san_pablo.adicionar_estudiante(e2)
san_pablo.adicionar_estudiante(e3)
san_pablo.adicionar_estudiante(e4)
san_pablo.adicionar_estudiante(e5)
san_pablo.mostrar_estudiantes()

# %%

class solicitud:
    estudiante = ""
    profesor = ""
    hora = ""
    
    def __init__(self, nombre_estudiante, nombre_profesor, hora):
        self.estudiante = nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora
        
class Agenda:
    def __init__(self):
        self.solicitud: list[solicitud] = []
        
    def disponibilidad (self, profesor:str, hora:str) ->bool:
        for solicitud in self.solicitud:
            if (solicitud.profesor == profesor) and (solicitud.hora == hora):
                print("el profesor no esta disponible en esta hora")
                return False
        print("el profesor se encuentra disponible en esta hora")
        return True
    def agregar_turno(self, estudiante:str, profesor:str, hora:str)-> bool:
        if(self. disponibilidad(profesor, hora)==True):
            self.solicitud.append(solicitud(estudiante, profesor, hora))
            return True
        return False
    
    def eliminar_turno(self, profesor:str, hora:str):
        for profe, solicitud in enumerate(self.solicitud):
            if (solicitud.profesor == profesor) and (solicitud.hora == hora):
                del self.solicitud[profe]
                return True
        print("No hay ninguna tutoria agendada para el profesor a esta hora")
        return False
    
    def mostrar_turno(self):
        if (not self.solicitud):
            print("La agenda está vacía")
            return
        
        print("-----------Tutorias-----------")
        for solicitud in self.solicitud:
            print(f"-{solicitud. hora} \t {solicitud.profesor} \t {solicitud.estudiante} \t")
            
# %%
            
agenda = Agenda()
agenda.mostrar_turno()
agenda.agregar_turno("roger", "miller", "14:00")
agenda.agregar_turno("wilfredo", "jorge", "09:00")
agenda.disponibilidad("miller", "14:00")
agenda.agregar_turno("nicolas", "miller", "09:00")
agenda.mostrar_turno()
agenda.eliminar_turno("miller", "14:00")
agenda.mostrar_turno()
