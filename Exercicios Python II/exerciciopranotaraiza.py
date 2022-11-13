# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:44:01 2020

@author: ENGCOMP

"""
w= float( input("Digite o valor de w:"))
z= float(input("Digite o valor de z:"))

if w == 0 and z == 0:
    print("O valor esta na origem ")
    
elif w > 0 and z > 0:
    print("o valor esta no primeiro quadrante")
elif w < 0 and z > 0:
    print ("o valor esta no segundo quadrante")
elif w < 0 and z < 0:
    print("o valor esta no terceiro quadrante")
elif w > 0 and z < 0:
    print ("o valor esta no quarto quadrante")
elif w == 0 or z == 0:
   print("algum dos valores estao no eixo") 
