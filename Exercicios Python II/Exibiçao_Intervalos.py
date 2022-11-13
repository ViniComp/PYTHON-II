# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:58:20 2020

@author: ENGCOMP
"""

# Exibindo os valores de 0 a 20

for i in range(21):
    print(i)
    
# Exibindo valores de 14 a 32
print ("valor de 14 a 32")
for valor in range(14,33):
    print (valor)
    
print ("O valor abaixo é definido por 0 a 99 de 5 em 5")

for intervalo in range (0,100,5):
    print (intervalo)
    
print("Exibindo letra a letra de um texto (string)")
    
#Exibindo letra a letra de um nome
nome= input("Iforme um nome qualquer:")

for letra in nome:
    print (letra)