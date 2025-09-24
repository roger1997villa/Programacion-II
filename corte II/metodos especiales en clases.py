# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 07:35:41 2025

@author: roger
"""

class Contenedor:
    def __init__(self):
        self.datos = {}

    def __getitem__(self, key):
        return self.datos[key]

    def __setitem__(self, key, value):
        self.datos[key] = value

c = Contenedor()
c['a'] = 100
print(c['a'])  # 100
#%%
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.f = open(self.nombre, "w")
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()

with Archivo("asistencias.txt") as asit_20sep:
    asit_20sep.write("Hola mundo\nNicolas -ok\nFelipe -ok\nRoger -ok\nWilfredo -ok")