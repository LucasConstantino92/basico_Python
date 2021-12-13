# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:28:12 2021

@author: luconstantino

23 

"""

fahr = int(input("Digite os graus em Fahrenheit: "))

fahr1 = float((fahr - 32) / 9)
celsius = fahr1 * 5

print(fahr,"graus Fahrenheit são",celsius,"graus Celsius.")
