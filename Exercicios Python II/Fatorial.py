# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:27:35 2020

@author: ENGCOMP
"""

# Faça um programa que leia um número e calcule seu Fatorial. 

numero =  input ("Digite o numero para saber o fatorial:")

if numero.isnumeric():
    numero = int (numero)
    f = 1
    
    for num in range(1, numero +1):
        f = num * f
        
        print ("o espaco final é:", f)
else:
    
 print("Entrada invalida")