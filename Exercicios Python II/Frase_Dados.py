# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:29:30 2020

@author: ENGCOMP
"""

##Manipulando variaveis string atraves de funçoes
##len() - > o tamanho da frase!
##upper() -> deixa o texto todo em maisculo
## lower () -> deixa o texto todo em minusculo

# Declarando variaveis!
frase = ""

frase = input("Digite um frase qualquer:")

#Descobrindo o tamanho da frase
tamanho = len(frase)

print("O tamanho da frase é :", tamanho)

#Deixando todas as letras em minusculo
frase = frase.lower()
print("A frase em caixa baixa é :", frase)
#Deixando todas as letras em maiusculo
frase = frase.upper()
print("A frase em caixa alta é:", frase)
