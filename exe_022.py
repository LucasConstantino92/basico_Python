# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:08:04 2021

@author: luconstantino

22 - Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Crie um programa que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vende-dor.
"""

salario = int(input("Digite o salário pago: R$ "))
comissao = int(input("Digite a porcentagem da comissão fixa: "))
VendidosFunc = int(input("Digite o valor vendido pelo funcionario no mês: R$ "))
carrosVendidosGeral = int(input("Digite o valor de vendas no geral: R$ "))

comissaoFuncGeral = int(carrosVendidosGeral * (comissao / 100))
comissaoFuncVendas = int(VendidosFunc * 0.05)

comissaoFuncFinal = f'{comissaoFuncGeral:.2f}'
comissaoVendasFinal = f'{comissaoFuncVendas:.2f}'
salarioParc = salario + (comissaoFuncGeral + comissaoFuncVendas)

salarioFinal = f'{salarioParc:.2f}'

print("O salário final do funcionário é de R$",salarioFinal,", o valor da comissão por carros vendidos no geral é de R$",comissaoFuncFinal,"e o valor da comissão pelas vendas do funcionário é de R$",comissaoVendasFinal)
