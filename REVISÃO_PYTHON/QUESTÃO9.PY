'''
QUESTÃO9. Escreva um programa que leia um número inteiro n 
e mostre a tabuada de multiplicar de n.'''

n = int(input('Digite um número inteiro: '))
print('')
print(f'Tabuada de {n}:')
control = 0
while  control < 10:
    control+=1
    multiply = control*n
    print(f'{control} x {n} = {multiply}')
print('')