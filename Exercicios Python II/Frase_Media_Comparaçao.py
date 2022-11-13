# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:14:49 2020

@author: ENGCOMP
"""

#Peça ao seu usuario que informe 4 fases.
# a) descubra a media dos tamanhos das frases;
# b) descubra qual frase é a maior;
# c) exiba a maior frase em minuscula

## Declaração das variaveis!!

#frase_1 = ""
#frase_2 = ""
#frase_3 = ""
#frase_4 = ""

frase_1 = input("Frase 1:")
frase_2 = input("Frase 2:")
frase_3 = input("Frase 3:")
frase_4 = input("Frase 4:")


## Descobrindo os tamanhos!
tamanho_1 = len(frase_1)
tamanho_2 = len(frase_2)
tamanho_3 = len(frase_3)
tamanho_4 = len(frase_4)

media = ( tamanho_1 + tamanho_2 + tamanho_3 + tamanho_4) / 4

print("A  media dos tamanhos é:", media)

if tamanho_1 > tamanho_2 and tamanho_1 > tamanho_3 and tamanho_1 > tamanho_4:
    frase_1 = frase_1.lower()
    print("A frase em minusculo é:", frase_1)
    print("O tamanho é :", tamanho_1)
elif tamanho_2 > tamanho_1 and tamanho_2 > tamanho_3 and tamanho_2 > tamanho_4:
    frase_2 = frase_2.lower()
    print("A frase em minusculo é:", frase_2)
    print("O tamanho é :", tamanho_2)
elif tamanho_3 > tamanho_1 and tamanho_3 > tamanho_2 and tamanho_3 > tamanho_4:
    frase_3 = frase_3.lower()
    print("A frase em minusculo é:", frase_3)
    print("O tamanho é :", tamanho_3)
elif tamanho_4 > tamanho_1 and tamanho_4 > tamanho_2 and tamanho_4 > tamanho_3:
    frase_4 = frase_4.lower()
    print("A frase em minusculo é:", frase_4)
    print("O tamanho é :", tamanho_4)
else:
    print("Ha frases com tamanhos identicos!!!")
