# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 10:39:45 2025

@author: roger
"""
import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_tipo(self):
        print(f"Soy un {self.nombre}")
        

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("círculo")
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def mostrar_dimensiones(self):
        print(f"Círculo de radio: {self.radio}")
        print(f"Perímetro: {self.perimetro():.2f}")
        print(f"Área: {self.area():.2f}")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("rectángulo")
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def mostrar_dimensiones(self):
        print(f"Rectángulo de {self.base} x {self.altura}")
        print(f"Perímetro: {self.perimetro()}")
        print(f"Área: {self.area()}")


# --- Ejemplos de uso ---
cir = Circulo(7)
cir.mostrar_tipo()
cir.mostrar_dimensiones()



rect = Rectangulo(5, 3)
rect.mostrar_tipo()
rect.mostrar_dimensiones()