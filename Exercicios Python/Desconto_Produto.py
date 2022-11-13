preço = float(input('Informe o preço do produto: '))
desconto = preço - (5/100) * preço
print('O valor do produto com 5% de desconto é de {:.2f}'.format(desconto))