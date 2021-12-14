# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:23:47 2021

@author: luconstantino

27 - Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um programa em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina in-forme quanto será o valor arrecadado.
"""

p = int(input("Quantas camisas P foram vendidas: "))
m = int(input("Quantas camisas M foram vendidas: "))
g = int(input("Quantas camisas G foram vendidas: "))

res = ((p * 10) + (m * 12) + (g * 15))

print("Foram vendidas",p,"camisas P,",m,"camisas M e",g,"camisas G. O valor total é de R$",res)
