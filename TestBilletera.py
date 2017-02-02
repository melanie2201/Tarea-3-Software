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
    
        
        