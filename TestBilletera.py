#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 1, 2017

@author: melanie

'''

from Billetera import *
import unittest 

class TestBilletera(unittest.TestCase):
    
    def testIdentificador(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.identificador, 1)
        
    def testNombre(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.nombre, "Melanie")
        
    def testApellido(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.apellido, "Gomes")
        
    def testCedula(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.cedula,23893494)
        
    def testPin(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.pin, 2212)
        
    def testInicializacion(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.disp, 0)
        
    def testConsumo(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.consumos.__len__(),0)
        
    def testRecargas(self):
        self.b= BilleteraElectronica(1,"Melanie","Gomes",23893494,2212)
        self.assertEqual(self.b.recargas.__len__(),0)

    def testFrontera(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(float(sys.maxint),"enero", 21332)
        self.b.consumir(float(sys.maxint), "enero", 2541,9929)
        self.assertEqual(self.b.disp,0)
    
    def testFrontera1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(float(sys.maxint),"enero", 2133)
        self.b.consumir(0.00 , "enero", 2541,9929)
        self.assertEqual(self.b.disp,float(sys.maxint))

    def testEsquina(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(600.00,"enero", 21332)
        self.b.consumir(599.00 , "enero", 2541,9929)
        self.assertEqual(self.b.disp,1)
    
    def testEsquina1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(600.00,"enero", 21332)
        self.b.consumir(1.00 , "enero", 2541,9929)
        self.assertEqual(self.b.disp,599)
        
    def testMalicia1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(300.00,"enero", 21332)
        #Esto debera lanzar una excepcion
        print("Prueba de malicia 1: ")
        self.b.consumir(550.30 , "enero", 2541,9929)
        print("------------------")
        
    def testMalicia2(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(300.00,"enero", 21332)
        #Esto debera lanzar una excepcion
        print("Prueba de malicia 2: ")
        self.b.consumir(250.0 , "enero", 2541,9989)
        print("------------------")
        
    def testMalicia3(self):
        print("Prueba de malicia 3: ")
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(-300.00,"enero", 21332)
        #Esto debera lanzar una excepcion    
        print("------------------")
        
    def testMalicia(self):
        
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(300000.00,"enero", 21332)
        self.b.consumir(10000.00, "enero", 2541,9929)
        self.assertEqual(self.b.disp,290000)
        