#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 1, 2017

@author: melanie Gomes 1310544
@author: Veronica Mazutiel 1310853

'''

from Billetera import *
import unittest 

#Casos de prueba para la clase Billetera

class TestBilletera(unittest.TestCase):
    
    #Prueba de inicializacion del identificador    
    def testIdentificador(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.identificador, 1)
    #Prueba de inicializacion del nombre    
    def testNombre(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.nombre, "Melanie")
    #Prueba de inicializacion del apellido    
    def testApellido(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.apellido, "Gomes")
    #Prueba de inicializacion de la cedula    
    def testCedula(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.cedula,23893494)
    #Prueba de inicializacion del pin    
    def testPin(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.pin, 2212)
    #Prueba de inicializacion del saldo disponible
    def testInicializacion(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.disp, 0)
    #Prueba de inicializacion del arreglo de consumos, debe estar vacio    
    def testConsumo(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.consumos.__len__(),0)
    #Prueba de inicializacion del arreglo recargas, debe estar vacio    
    def testRecargas(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.recargas.__len__(),0)
    #Caso frontera, con recarga del maximo valor posible y consumir la 
    #totalidad del saldo disponible
    def testFrontera(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(float(sys.maxint),"enero", 21332)
        self.b.consumir(float(sys.maxint), "enero", 2541,9929)
        self.assertEqual(self.b.disp,0)
    #Caso frontera, con recarga del maximo valor posible y no consumir 
    #nada del saldo disponible
    def testFrontera1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(float(sys.maxint),"enero", 2133)
        self.b.consumir(0.00 , "enero", 2541,9929)
        self.assertEqual(self.b.disp,float(sys.maxint))
    #Caso de esquina, haciendo una recarga de 600 y consumiendo casi la
    #totalidad del saldo disponible, dejando un saldo de 1
    def testEsquina(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(600.00,"enero", 21332)
        self.b.consumir(599.00 , "enero", 2541,9929)
        self.assertEqual(self.b.disp,1)
    #Caso de esquina, haciendo una recarga de 600 y consumiendo exactamente
    # 1.00 del saldo disponible, dejando un saldo de 599
    def testEsquina1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(600.00,"enero", 21332)
        self.b.consumir(1.00 , "enero", 2541,9929)
        self.assertEqual(self.b.disp,599)
        
    #Caso de malicia en la que se intenta consumir mas del saldo disponible
    #lanza una excepcion en la cual se expresa que el saldo disponible no es
    #suficiente para hacer la transaccion
    def testMalicia1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(300.00,"enero", 21332)
        #Esto debera lanzar una excepcion
        print("Prueba de malicia 1: ")
        self.b.consumir(550.30 , "enero", 2541,9929)
        print("------------------")

    #Caso de malicia en la que se intenta consumir introduciendo el pin 
    #equivocado, lanza una excepcion en la cual se expresa que el pin que 
    #se introdujo es incorrecto
    def testMalicia2(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(300.00,"enero", 21332)
        #Esto debera lanzar una excepcion
        print("Prueba de malicia 2: ")
        self.b.consumir(250.0 , "enero", 2541,9989)
        print("------------------")
    #CASO de malicia en la cual se intenta hacer una recarga con un monto
    #negativo, lanza una excepcion que dice que el monto de recarga no puede
    #ser negativo 
    def testMalicia3(self):
        print("Prueba de malicia 3: ")
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(-300.00,"enero", 21332)
        #Esto debera lanzar una excepcion    
        print("------------------")
      
    #Caso interior para verificar que se esten haciendo las recargas
    #y los consumos de manera correcta  
    def testMalicia(self):
        
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(300000.00,"enero", 21332)
        self.b.consumir(10000.00, "enero", 2541,9929)
        self.assertEqual(self.b.disp,290000)
        