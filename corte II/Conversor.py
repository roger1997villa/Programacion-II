# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 06:22:07 2025

@author: roger
"""
class Conversor:
    # Atributos 
    def __init__(self, num, base_origen, base_final):
        self.__num = num
        self.__base_origen = base_origen
        self.__base_final = base_final
    
    # Método: convertir a decimal
    def conver_decimal(self):
        try:
            num_decimal = int(self.__num, self.__base_origen)
            print(f"{self.__num} (base {self.__base_origen}) convertido a decimal es {num_decimal}")
        except ValueError:
            print("El número ingresado no es válido para la base ingresada")
    
    # Método: convertir a binario
    def conver_binario(self):
        try:
            num_decimal = int(self.__num, self.__base_origen)
            num_binario = bin(num_decimal)[2:]
            print(f"{self.__num} (base {self.__base_origen}) convertido a binario es {num_binario}")
        except ValueError:
            print("El número ingresado no es válido para la base ingresada")
    
    # Método: convertir a octal
    def conver_octal(self):
        try:
            num_decimal = int(self.__num, self.__base_origen)
            num_octal = oct(num_decimal)[2:]
            print(f"{self.__num} (base {self.__base_origen}) convertido a octal es {num_octal}")
        except ValueError:
            print("El número ingresado no es válido para la base ingresada")
    
    # Método: convertir a hexadecimal
    def conver_hexa(self):
        try:
            num_decimal = int(self.__num, self.__base_origen)
            num_hexa = hex(num_decimal)[2:]
            print(f"{self.__num} (base {self.__base_origen}) convertido a hexadecimal es {num_hexa}")
        except ValueError:
            print("El número ingresado no es válido para la base ingresada")
    
    # Método general
    def convertir(self):
        if self.__base_final == 10:
            self.conver_decimal()
        elif self.__base_final == 2:
            self.conver_binario()
        elif self.__base_final == 8:
            self.conver_octal()
        elif self.__base_final == 16:
            self.conver_hexa()
        else:
            print("La base final no es válida")


# ----------------- MENÚ -----------------

def menu():
    while True:
        print( "Conversor de Sistemas Numéricos ")
        num = input("Ingrese el número que desea convertir: ")
        base_origen = int(input("Base de origen\n 2 = Binario\n 8 = Octal\n 10 = Decimal\n 16 = Hexadecimal\n :  "))
        base_final = int(input("Base final 2, 8, 10, 16: "))
        
        # Crear el objeto con los datos del usuario
        c = Conversor(num, base_origen, base_final)
        
        # Realizar conversión
        c.convertir()
        
        # Preguntar si desea continuar
        opcion = input("\n¿Desea hacer otra conversión? (s/n): ")
        if opcion.lower() != "s":
            print("¡Gracias por usar el conversor! 😎")
            break
        
        
        #%%
menu()