'''
QUESTÃO4. Brincadeira do ímpar ou par: escreva um programa que leia dois nomes e dois valores inteiros, 
que correspondem ao que cada um colocou, e informe quem ganhou o “ímpar ou par”.'''


jogador1 = input('Digite o nome do jogador 1 : ')
numerodojogador1 = int(input('Muito bem, '+ jogador1 +', Agora digite um número : '))

jogador2 = input('Digite o nome do jogador 2 : ')
numerodojogador2 = int(input('Muito bem, '+ jogador2 +' , Agora digite um número: '))
soma = numerodojogador2 + numerodojogador1
if (soma % 2 == 0):
    print ('O par ganhou!')
else:
    print ('O ímpar ganhou!')