# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 06:17:32 2025

@author: casa
"""

try:
    resultado = 10 / 0
    
except ZeroDivisionError:
    print("!! error, no se puede dividir entre cero")
    
    
    
try: 
    num = int(input("ingrese un numero: "))
    
except ValueError:
    print("debes ingresar un numero valido")
else: 
    print(f"el numero ingresado es {num}")
    
    
    
try: 
    archivo = open("datos txt", "y")
    contenido = archivo.read()
except FileNotFoundError:
    print("el archivo no existe")
    
finally:
    archivo.close()
        
try:
    num = int(input("ingrese un numero: "))
    print(10 / num)
    
except ValueError:
    print("debe ser un numero")
except ZeroDivisionError:
    print("error, no se puede dividir por cero")
else:
    print(f"el numero ingresado es {num}")
    print(f"la division es  {10 / num}")
    

def dividir_numeros():
    try:
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese  el segundo numero: "))
        resultado = num1 / num2
    except ValueError:
        print("Error, ingrese numeros validos")
    except ZeroDivisionError:
        print("Error, no se puede dividir entre cero")
        
    else:
        print(f"el resultado es {resultado}")
        
    finally:
        print("fin del programa")
        
        
        
dividir_numeros()
