# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:25:41 2020

@author: ENGCOMP
"""

numero_empresas = input("Digite o numero de empresas:")
soma= 0
sem_dividas=0
if numero_empresas.isnumeric():
    numero_empresas = int (numero_empresas)
    
    for emp in range(numero_empresas):
        divida = input ("informe a divida:")
        divida = float (divida)
        soma= soma+divida 
        if divida == 0:
            print ("A empresa",emp +1 ,"nao possui dividas")
            sem_dividas = sem_dividas +1
            
            
    media= soma / (numero_empresas - sem_dividas)
    
    print ("A media é:",media)
    