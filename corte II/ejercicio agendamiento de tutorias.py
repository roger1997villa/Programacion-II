# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 07:58:57 2025

@author: roger
"""

class Solicitud:
    def __init__(self, nombre_estudiante, nombre_profesor, hora):
        self.estudiante = nombre_estudiante
        self.profesor = nombre_profesor
        self.hora = hora

class Agenda:
    def __init__(self):
        self.solicitudes: list[Solicitud] = []
        
    

    def disponibilidad(self, profesor: str, hora: str) -> bool:
        for solicitud in self.solicitudes:
            if solicitud.profesor == profesor and solicitud.hora == hora:
                print(" El profesor NO está disponible en esta hora")
                return False
        print(" El profesor está disponible en esta hora")
        return True

    def agregar_turno(self, estudiante: str, profesor: str, hora: str) -> bool:
        if self.disponibilidad(profesor, hora):
            self.solicitudes.append(Solicitud(estudiante, profesor, hora))
            print("Turno agregado con éxito")
            return True
        return False

    def eliminar_turno(self, profesor: str, hora: str):
        for idx, solicitud in enumerate(self.solicitudes):
            if solicitud.profesor == profesor and solicitud.hora == hora:
                del self.solicitudes[idx]
                print(" Turno eliminado correctamente")
                return True
        print(" No hay ninguna tutoría agendada para el profesor en esa hora")
        return False

    def mostrar_turno(self):
        if not self.solicitudes:
            print("La agenda está vacía")
            return
        print("\n----------- Tutorías -----------")
        for solicitud in self.solicitudes:
            print(f"- {solicitud.hora} \t {solicitud.profesor} \t {solicitud.estudiante}")
        print("--------------------------------")


profesores = ["Arley", "Luisa", "Jorge", "Liliana", "Miller", "César"]
agenda = Agenda()


def menu_profesores():
    print("\n--- Seleccione un profesor ---")
    print("1. Arley\n2. Luisa\n3. Jorge\n4. Liliana\n5. Miller\n6. César")

    try:
        opcion = int(input("Ingrese el número del profesor: "))
    except ValueError:
        print(" Ingrese un número válido")
        

    match opcion:
        case 1: return "Arley"
        case 2: return "Luisa"
        case 3: return "Jorge"
        case 4: return "Liliana"
        case 5: return "Miller"
        case 6: return "César"
        case _:
            print(" Profesor no válido")
            return None


while True:
    print("\n===== MENÚ AGENDA DE TUTORÍAS =====")
    print("1. Ver disponibilidad")
    print("2. Agregar turno")
    print("3. Eliminar turno")
    print("4. Mostrar agenda")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print(" Ingrese un número válido")
        continue

    match opcion:
        case 1:
            profesor = menu_profesores()
            if profesor:
                hora = input("Ingrese la hora : ")
                agenda.disponibilidad(profesor, hora)

        case 2:
            estudiante = input("Ingrese el nombre del estudiante: ")
            profesor = menu_profesores()
            if profesor:
                hora = input("Ingrese la hora : ")
                agenda.agregar_turno(estudiante, profesor, hora)

        case 3:
            profesor = menu_profesores()
            if profesor:
                hora = input("Ingrese la hora a eliminar: ")
                agenda.eliminar_turno(profesor, hora)

        case 4:
            agenda.mostrar_turno()

        case 5:
            print(" Saliendo del sistema...")
            break

        case _:
            print(" Opción no válida, intente de nuevo.")