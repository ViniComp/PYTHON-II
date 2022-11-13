import math
ang = float(input('Digite o valor do angulo: '))
seno = (math.sin(math.radians(ang)))
coss = (math.cos(math.radians(ang)))
tang = (math.tan(math.radians(ang)))
print('O angulo de {}graus tem o SENO de {:.2f}graus'.format(ang,seno))
print('O angulo de {}graus tem o COSSENO de {:.2f}graus'.format(ang,coss))
print('O angulo de {}graus tem a TANGENTE de {:.2f} graus'.format(ang,tang))