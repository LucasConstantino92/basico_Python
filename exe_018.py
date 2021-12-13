# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 08:02:05 2021

@author: luconstantino

18 - Crie um programa para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores;
"""

eleitores = int(input("Digite o total de eleitores do município: "))
validos = int(input("Digite o total de votos validos: "))
brancos = int(input("Digite o total de votos brancos: "))
nulos = int(input("Digite o total de votos nulos: "))

resVal = float((validos * 100) / eleitores)
resBran = float((brancos * 100) / eleitores)
resNul = float((nulos * 100) / eleitores)

resVal1 = f'{resVal:_.2f}'
resBran1 = f'{resBran:_.2f}'
resNul1 = f'{resNul:_.2f}'

print("O município tem um total de",eleitores,"eleitores, aonde os votos válidos foram de",resVal1,"%, os votos brancos de",resBran1,"%e os votos nulos de",resNul1,"%")
