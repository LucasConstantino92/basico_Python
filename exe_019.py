# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:46:38 2021

@author: luconstantino

19 - Crie um programa para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário;
"""

salario = float(input("Digite o salário: "))
aumento = float(input("Digite a parocentagem(%) do aumento: "))

valorAumento = salario * (aumento / 100)
novoSalario = salario + valorAumento

print("O novo salário será de R$",novoSalario)
