# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:12:59 2021

@author: luconstantino

20 - Crie um programa para converter uma quantidade de dólar para real;
• O usuário deve informar o valor em dólar;
• O programa deve converter esse valor em reais, exibindo a mensagem com o valor convertido;
• DÓLAR: R$ 6.61;
"""

real1 = float(6.61)

valor = float(input("Digite o valor em Dólares que deseja converter em Reais: "))

resParcial = valor * real1

res = f'1{resParcial:.2f}'

print("O valor em reais é de R$:",res)
