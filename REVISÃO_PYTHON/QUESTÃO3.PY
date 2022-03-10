'''
QUESTÃO3.Escreva um programa leia dois nomes de times de futebol, a quantidade de gols do primeiro time, 
a quantidade de gols do segundo time e mostre o nome do time vencedor da partida.
'''
time1 = input('Digite o nome do primeiro time: ')
golsdotime1 = int(input('Digite o número de gols do time ' + time1 + ' :'))

time2 = input('Digite o nome do segundo time: ')
golsdotime2 = int(input('Digite o número de gols do time ' + time2 + ' :'))

if (golsdotime1 > golsdotime2):
    print ('O time vencedor é ' + time1)
else:
    print ('O time vencedor é ' + time2)