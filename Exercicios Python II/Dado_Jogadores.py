import random
import time

dados = {}

dados ['jogador1'] = random.randint(1,6)
dados ['jogador2'] = random.randint(1,6)
dados ['jogador3'] = random.randint(1,6)
dados ['jogador4'] = random.randint(1,6)


#print(dados)




for k,v in dados.items():
    print(k,'=',v)
    time.sleep(2)
    