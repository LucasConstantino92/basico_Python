# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:53:18 2021

@author: luconstantino

25 - Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um programa para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
"""

precoLitro = float(input("Digite o valor do combustível: R$ "))
valorPago = float(input("Digite o valor pago: R$ "))

litrosParcial = valorPago / precoLitro
litrosFinal = f'{litrosParcial:.1f}'

print("A quantidade de litros abastecidos foram de",litrosFinal)
