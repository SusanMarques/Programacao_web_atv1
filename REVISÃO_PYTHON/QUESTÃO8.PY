'''
QUESTÃO8. Escreva um programa que mostre todos os números entre 1 e 100 que 
são múltiplos de 3 e 7.'''

num=1
print('Múltiplos de 3 e 7 entre 1 e 100:')
while num < 100:
    num+=1
    if (num % 3 == 0 and num % 7 == 0):
        print(num)