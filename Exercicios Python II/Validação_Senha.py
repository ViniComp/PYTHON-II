# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:12:43 2020

@author: ENGCOMP
"""
# A REGRA DO EXERCICIO == DIGITOS:3== LETRAS:5

senha= input("informe a senha:")
contagem_numeros=0
contagem_letras=0

for letra in senha:
    if letra.isnumeric():
        contagem_numeros = contagem_numeros+1
    elif letra.isalpha():
        contagem_letras = contagem_letras+1
        
if contagem_letras == 5 and  contagem_numeros == 3:
    print("A senha e valida!!")
    
else :
    print("Senha invalida")