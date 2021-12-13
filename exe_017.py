# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 07:51:15 2021

@author: luconstantino

17 - Crie um programa para ler a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dia. Considerar ano com 365 dias e mês com 30 dias
"""

print("Digite qual sua idade em anos, meses e dias.")

anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite quantos meses: "))
dias = int(input("Digite quantos dias: "))

resultado = (anos * 365) + (meses * 30) + dias

print("Você já viveu ", resultado, "dias")