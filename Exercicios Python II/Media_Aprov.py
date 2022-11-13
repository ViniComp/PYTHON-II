# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:50:09 2020

@author: ENGCOMP
"""
#Exerciico 5
##Essa variavel vai servir como controle de execucao
media=0

while media >= 0:
    media = input ("Digite a media:")
    
    if not media.isalpha():
        media= float (media)
        if media>= 0 and media < 3:
            print("Voce reprovou!!!")
        elif media>= 3 and media <5:
            print ("Voce esta de recuperacao")
        elif media>= 5 and media <=10:
            print ("VOCE ESTA APROVADO")
else :
 print ("O PROGRAMA FOI ENCERRADO")