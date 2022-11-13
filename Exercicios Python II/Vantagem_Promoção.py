# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:25:14 2020

@author: ENGCOMP
"""

## Exercicio dos criterios - lista 1
## ex 2


quantidade = input( "Informe  a quantidade  de livros :")

if quantidade. isnumeric():
    
    quantidade = int (quantidade)
    
    if quantidade > 0:
    
        criterio_a = 0.25 * quantidade + 7.50
        
        criterio_b = 0.50 * quantidade + 2.50
        
        if criterio_a < criterio_b:
            print ("A promoçao A é mais vantajosa e voce pagara;", criterio_a)
        elif criterio_b < criterio_a:
            print (" A promoção B é mais vantajosa e voce pagara:", criterio_b)
        else:
            print(" Voce pode escolher qualquer dos criterios!")
    else:
       print("Entrada nula ou negativa! tente novamente!")
else:
    print("Entrada invalida! Repita a operação !")
