# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:23:24 2021

@author: luconstantino

21 - O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, crie uma programa para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

"""

carroFabrica = float(input("Valor de de fábrica: R$ "))

distrib = float(carroFabrica * 0.28)
imposto = float(distrib * 0.45)
valorSoma = float(carroFabrica + distrib + imposto)

valorFinal = f'{valorSoma:.2f}'

print("O valor do carro para o consumidor é de R$:",valorFinal)
