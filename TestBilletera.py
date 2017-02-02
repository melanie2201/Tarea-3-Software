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
        
    def testprueba(self):     
    
        
        