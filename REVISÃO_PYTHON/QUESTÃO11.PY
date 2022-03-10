'''
QUESTÃO11. Escreva um programa que uma sequência de nomes e mostre-os em ordem alfabética. 
O programa deve parar de ler quando o usuário digitar fim.
'''

control = 0
nome = 0
words_list = []
while nome != 'fim':
    nome = str(input('Digite um nome: '))
    if nome == 'fim':
        break
    else:
        words_list.append(nome)
print(f'nomes em ordem alfabética: {sorted(words_list)}')