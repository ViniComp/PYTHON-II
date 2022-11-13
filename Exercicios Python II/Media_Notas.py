# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:59:00 2020

@author: ENGCOMP
"""

nome_aluno =("Informe o seu nome:")
nota_um = float(input("Informe a nota P1:"))
nota_dois = float(input("Informe a nota P2:"))

media = (nota_um + (2 * nota_dois) ) / 3

if media <3 :
    print("Ate breve, querido aluno!")
elif media > 3 and media < 5 :
    print("Voce podera escapar! Força!")
    faltante = 5 - media
    print("Falta para voce passar:", faltante)  
else :          
    print("Parabens, ate nunca mais!")
    
    