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
        
        
    def saldo(self):
        return self.disp
        
    def recargar(self,monto,fecha,id):
         #Verificaciones de tipo
        try:
            assert(type(fecha) is str  and type(id) is int and type(monto) is float)
        except:
            print("Tipo de datos inválidos para hacer la recarga.")
            return
        #Verificar que el monto a recargar sea positivo   
        try: 
            assert(monto>0)
        except:
            print("La recarga debe ser de un moto positivo")
        
        self.disp+=monto;
        self.recargas.append([monto,fecha,id]) 
        
    def consumir(self,monto,fecha,id,pinDado):
        #Verificaciones de tipo
        try:
            assert(type(fecha) is str  and type(id) is int and type(monto) is float and type(pinDado) is int)
        except:
            print("Tipo de datos inválidos para hacer la recarga.")
            return
        #Verificacion de pin
        try:
            assert(pinDado==self.pin)
        except:
            print("Pin inválido")
            return
        #Verificacion de saldo disponible par hacer la operacion
        try: 
            assert(monto<=self.saldo())
        except:
            print("Saldo insuficiente.")
            return
        
        self.disp-=monto
        self.consumos.append([monto,fecha,id])
        
        #Funciones no solicitadas, hechas para revisar lista de recargas y consumos    
    def listaRecargas(self):
        for i in range(len(self.recargas)):
            print( self.recargas[i])
            
    def listaConsumos(self):
        for i in range(len(self.consumos)):
            print( self.consumos[i])

        
