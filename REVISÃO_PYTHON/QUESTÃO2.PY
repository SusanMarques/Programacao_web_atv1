'''
QUESTÃO2. Faça um algoritmo que leia 3 números inteiros 
distintos e escreva o menor deles.

'''

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))
if ((num1 < num2) and (num1 < num3)):
    print ('O menor número é:', num1)
if ((num2 < num1) and (num2 < num3)):
    print ('O menor número é:', num2)
if ((num3 < num2) and (num3 < num1)):
    print ('O menor número é:', num3)