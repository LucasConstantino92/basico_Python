# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:40:58 2021

@author: luconstantino

24 - Crie um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.

"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado = ((nota1 * 2)+ (nota2 * 3) + (nota3 * 5))/10

print("A média final do aluno é",resultado)
