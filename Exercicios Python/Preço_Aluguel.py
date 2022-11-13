dia = int(input('Digite o número de dias que o carro foi alugado: '))
km = float(input('Digite os quilometros rodados: '))
valor1 = km * 0.15
valor2 = dia * 60
print('O preço a pagar pelo aluguel é de R${:.2f}'.format(valor1+valor2))