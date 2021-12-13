# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:18:46 2021

@author: luconstantino

09 - Crie um programa que receba dois valores do usuário e exiba a o resultado de sua soma;
10 - Crie um programa que receba dois valores do usuário e exiba a o resultado de sua subtração;
11 - Crie um programa que receba dois valores do usuário e exiba a o resultado de sua multiplicação;
12 - Crie um programa que receba dois valores do usuário e exiba a o resultado de sua divisão;
13 - Crie um programa com uma ou duas variáveis atribu-indo valores iniciais e exiba a o resultado de sua exponenciação;
14 - Crie um programa com uma ou duas variáveis atribu-indo valores iniciais e exiba a o resultado do módulo entre eles;
"""
valorUm = int(input("Digite o primeiro valor: "))
valorDois = int(input("Digite o segundo valor: "))
operacao = input("Digite a operação que deseja fazer: 1 para soma, 2 para subtração, 3 para divisão, 4 para multiplicação, 5 para módulo e 6 para exponenciação.")

if(operacao == '1'):
    print("O resultado da soma é: ", valorUm + valorDois)
elif(operacao == '2'):
    print("O resultado da subtração é: ", valorUm - valorDois)
elif(operacao == '3'):
    print("O resultado da multiplicação é: ", valorUm * valorDois)
elif(operacao == '4'):
    print("O resultado da divisão é: ", valorUm / valorDois)
elif(operacao == '5'):
    print("O resultado do módulo é: ", valorUm % valorDois)
else:
    print("O resultado da exponenciação é: ", valorUm ** valorDois)