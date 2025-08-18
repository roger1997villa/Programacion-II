# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:20:36 2025

@author: AULA
"""
print("""
      opcion 1 : Reclamos y peticiones 
      opcion 2 : Planes
      opcion 3 : Saldo de tu cuenta 
      opcion 4 : Consultar factura 
      opcion 5 : Cancelacion de servicio
      opcion 6 : Descargar fdactura 
      opcion 7 : Pago via telefonica 
      opcion 7 : Comunicarse con un asesor 
      opcion 8 : Comunicarse con un asesor 
      opcion 9 : Adquirir nueva linea
      opcion 0 : Finalizar llamada
      """)

opcion = int(input("Digite su opcion: "))

match opcion:
    case 1: 
        print("Opcion de reclamos y peticiones")
    case 2:
        print("Opcion de planes prepago y pos pago")
    case 3 :
        print("su saldo de la cuenta es de $52.012")
    case 4 :
        print("Factura disponible para descargar")
    case 5 :
        print("Opcion de cancelacion de su servicio pospago")
    case 6 :
        print("Oprime * para descargar factura")
    case 7 :
        print("Cual es su medio de pago")
    case 8 :
        print("Comunicarse con su asesor, no cuelgue la llamada")
    case 9 :
        print("Desea adquirir una linea prepago/pospago")
    case 0 :
        print("Gracias por haberse comunicado con nosotros. Hasta pronto...!!!")       
    case _ :
        print("Opcion no valida")
        
#%%
print("Hola, bienvenido")

print("""
      opcion 1 : suma valor a y b  
      opcion 2 : resta valor a - b 
      opcion 3 : multiplicacion valor a * b 
      opcion 4 : divicion valos a / b 
      opcion 5 : divicion valos b / a 
      opcion 6 : potencia valor a ^ b  
      opcion 7 : potencia valor b ^ a 
      """)

a = int(input("Digite un valor para a : "))

b = int(input("Digite un valor para b : "))

opcion = int(input("Digite su opcion: "))

match opcion:
    case 1: 
        print(f"suma: {a} + {b} = {a+b}")
    case 2:
        print(f"resta: {a} - {b} = {a-b}")
    case 3 :
        print(f"multiplicacion: {a} * {b} = {a*b}")
    case 4 :
        print(f"divicion: {a} / {b} = {a/b}")
    case 5 :
        print(f"division: {b} / {a} = {b/a}")
    case 6 :
        print(f"potencia: {a} ^ {b} = {a**b}")
    case 7 :
        print(f"potencia: {b} ^ {a} = {b**a}")
    case _ :
        print("Opcion no valida") 

print("Gracias pos su visita hasta pronto")
#%%
