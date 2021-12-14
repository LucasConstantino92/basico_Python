# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:33:37 2021

@author: luconstantino

28 - Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. Faça um programa para ler o valor total da conta e imprimir quanto cada um deve pa-gar, mas faça com que Carlos e André não paguem centa-vos. Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para André e R$35,53 para Felipe.
"""

conta = float(input("Digite o valor da conta: R$ "))

carlos = int(conta / 3)
andre = int(conta / 3)
felipeParc = float(conta - (carlos + andre))
felipe = round(felipeParc, 2)

print("O valor que Carlos pagará é de R$",carlos,", o de André é de R$",andre,"e o de Felipe é de R$",felipe)
