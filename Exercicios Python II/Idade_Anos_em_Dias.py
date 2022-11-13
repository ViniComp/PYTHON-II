# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:09:55 2020

@author: ENGCOMP
"""

##    DEFININDO UMA VARIAVEL
nome_completo = ""
idade = 0

## Realizando a leitura dos dados via teclado
nome_completo = input("Informe o seu nome: ")

## Exibindo o nome completo na tela
print("O nome informado foi :", nome_completo)

## Realizando a leitura de um dado via teclado
## e convertendo ele para inteiro!

idade = int (input("Digite a sua idade :"))

print ("A idade digitada foi: {}". format (idade))

idade_dias = idade * 360

print("A idade informada em dias é{}". format (idade_dias))