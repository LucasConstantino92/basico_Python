# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:04:53 2021

@author: luconstantino

26 - Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.
"""

print("Informe uma data!")
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês (Em números): "))
ano = int(input("Digite o ano: "))

if (mes == 1):
    res = dia
    print("Já se passaram",res,"dias desde o início do ano!")
else:
    res = (mes * 30) + dia
    print("Já se passaram",res,"dias desde o início do ano!")
