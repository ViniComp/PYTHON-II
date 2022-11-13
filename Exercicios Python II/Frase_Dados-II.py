# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:12:19 2020

@author: ENGCOMP
"""

frase= input ("Informe a frase testada:")

contagem_numerica= 0
contagem_letra=0
contagem_espacos=0

for simbolo in frase:
    if simbolo.isnumeric():
        contagem_numerica = contagem_numerica+1
    elif simbolo.isalpha():
        contagem_letra = contagem_letra+1
    elif simbolo == ' ':
        contagem_espacos = contagem_espacos +1

print ("A quantidade de letras é:",contagem_letra)        
print ("A quantidade de numeros é:",contagem_numerica)        
print ("A quantidade de espacos é:",contagem_espacos)   

caracte_especial =  len(frase) - (contagem_espacos + contagem_letra+ contagem_numerica) 

print("A quantidade de caracteres especiais e", caracte_especial)
        