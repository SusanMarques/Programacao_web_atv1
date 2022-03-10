'''
QUESTÃO12. Usando arrays, escreva um programa que lê 5 números 
inteiros e verifica se pelo menos um é par.
'''
array = []
control=0
number=0
while control < 5:
    number = int(input('Digite um número:'))
    control+=1
    if number % 2 == 0:
        array.append(number)

size = len(array)
print(f'existem {size} números que são par. São eles: {array} ')