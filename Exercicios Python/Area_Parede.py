largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
print('A parede tem:\nLARGURA = {} m\nALTURA = {} m\nAREA = {} m²'.format(largura,altura,area))
tinta = area / 2
print('Serão necessário {} litros de tintas para pintar essa parede de {} m²'.format(tinta,area))
