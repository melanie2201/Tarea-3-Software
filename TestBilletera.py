#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 1, 2017

@author: melanie

'''

from Billetera import BilleteraElectronica 
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
        self.b.recargar(500,"enero", 21332)
        self.b.consumir(500 , "enero", 2541,999)
        self.assertEqual(self.b.disp,0)
    
    def testFrontera1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(500,"enero", 21332)
        self.b.consumir(0 , "enero", 2541,999)
        self.assertEqual(self.b.disp,500)

    def testEsquina(self):
       self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(500,"enero", 21332)
        self.b.consumir(499 , "enero", 2541,999)
        self.assertEqual(self.b.disp,1)
    
    def testEsquina1(self):
        self.b = BilleteraElectronica(1,'vero', 'mazu', 1231523, 9929)
        self.b.recargar(500,"enero", 21332)
        self.b.consumir(1 , "enero", 2541,999)
        self.assertEqual(self.b.disp,499)
    
        
        