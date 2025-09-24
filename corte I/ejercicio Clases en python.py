# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 07:28:36 2025

@author: casa
"""

            
        #%%
        
    
            
class Financiera:
    # atributos
    def __init__(self):
        self.__movimiento = {
            "juan": {
                "01/02/2025": +5_000_000,
                "15/03/2025": -3_000_000,
                "24/04/2025": +500_000,
            },
            "federico": {
                "01/02/2025": +3_000_000,
                "15/03/2025": -1_000_000,
                "24/04/2025": +200_000,
            }
        }
        print("Inicializadas las variables")

    def construccion(self):
        persona = input("Ingrese el cliente: ")
        if persona in self.__movimiento:
            print(f"\nMovimientos de {persona}:")
            print(f"{'Fecha':<12} | {'Monto':>10}")
            for fecha, monto in self.__movimiento[persona].items():
                print(f"{fecha:<12} | {monto:>10,}")
        else:
            print("Cliente no encontrado")

    def promedio(self, persona):
        if persona in self.__movimiento:
            valores = self.__movimiento[persona].values()  # toma solo los montos
            return sum(valores) / len(valores)
        else:
            return None

    def riesgo(self, persona):
        prom = self.promedio(persona)
        if prom is None:
            return "Cliente no encontrado"

        if prom < 0:
            return "Alto riesgo"
        elif prom < 10_000_000:
            return "Riesgo medio"
        else:
            return "Riesgo bajo"
        
        
        #%%
        
    cliente = Financiera()

cliente.construccion()   

print("\nPromedio Juan:", cliente.promedio("juan"))
print("Riesgo Juan:", cliente.riesgo("juan"))        
        