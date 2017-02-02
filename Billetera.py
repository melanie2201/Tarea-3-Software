#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Feb 1, 2017

@author: Melanie Gomes 
@author: Veronica Mazutiel
'''
import sys
class BilleteraElectronica:
    def __init__(self,identificador,nombre,apellido, cedula,pin):
        #Verificaciones de tipo
        try:
            assert(type(identificador) is int  and type(nombre) is str and type(apellido)\
                    is str and type(cedula) is int and type(pin) is int )
        except:
            print("Tipo de datos inválidos para la creación de la Billetera.")
            print("Tipos requeridos:\n-Identificador: int\n-Nombre:str\n-Apellido: str\n-Cedula: int\n-Pin: int\n")
            sys.exit()
        self.identificador=identificador
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.pin=pin
        self.recargas=[] 
        self.consumos=[] 
        self.disp=0
        
