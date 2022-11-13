# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:37:53 2020

@author: ENGCOMP
"""



valor_a= input ("Digite o valor: ")
valor_b= input ("Digite o valor: ")
valor_c= input ("Digite o valor: ")

if valor_a.isnumeric() and valor_b.isnumeric() and valor_c.isnumeric():
    valor_a = int(valor_a)
    valor_b = int(valor_b)
    valor_c = int(valor_c)
    
    mediaAB = (valor_a + valor_b + abs(valor_a-valor_b )) /2
    
    maior = (mediaAB + valor_c + abs(mediaAB-valor_c))/2
    
    print ("O maior valor entre {} e {} e {}".format (valor_a, valor_b, valor_c))
    print ("E o",maior )
    
else:
    print ("Entrada invalida")
    
    