'''
QUESTÃO5. Usando arrays, leia 5 números inteiros exiba-os 
ordenados do maior para o menor .'''

size = 6
control = 1
numbers = []
while control < size:
  number = int(input(f'Digite o {control}º número:'))
  control += 1
  numbers.append(number)

ordination = sorted(numbers, reverse=True)
print(f'Números ordenados do maior para o menor: {ordination}')