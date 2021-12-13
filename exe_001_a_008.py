# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:49:07 2021

@author: luconstantino

01 - Crie um programa para que apresente seu nome, seu celular e sua cidade;
02 - Crie um programa para que apresente sua idade, altura e peso;
03 - Crie um programa para que apresente seu salário e vale-refeição;
04 - Crie um programa declarando uma variável do tipo String chamada nome, outra chamada celular e outra cha-mada cidade, atribua um valor para todas as variáveis e exiba o resultado no console;
05 - Crie um programa declarando uma variável do tipo int chamada idade, outra chamada altura e outra peso, ambas do tipo double, atribua um valor para todas as variáveis e exiba o resultado no console;
06 - Crie um programa para que receba do usuário o nome, celular e cidade e exiba no console;
07 - Crie um programa para que receba do usuário o idade, altura e peso e exiba no console;
08 - Crie um programa para que receba do usuário o salá-rio e vale-refeição e exiba no console;
"""

nome = input("Escreva seu nome: ")
celular = int(input("Digite seu celular: "))
cidade = input("Digite sua cidade: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
salario = float(input("Digite seu salário: "))
vale = float(input("Digite seu Vale-Refeição: "))

sv = salario + vale

print("Seu nome é",nome,"seu celular é",celular,"e sua cidade é",cidade)
print("Você tem",idade,"anos, sua altura é",altura,"e o seu peso é",peso)
print("Você tem um salário de",salario,"reais, e o seu Vale-Refeição é de",vale,"totalizando",sv)
print("Obrigado!")