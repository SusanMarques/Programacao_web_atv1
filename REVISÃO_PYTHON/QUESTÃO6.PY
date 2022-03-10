'''
Questão6. Leia os dois primeiros números de um array de inteiros e depois calcule 
os 8 números seguintes do array. A regra é que os demais elementos são calculados 
somando os dois anteriores. Exiba o array usando print.'''

num = [int(input('Digite o primeiro numero:')),int(input('Digite o segundo numero:'))] 
control=0
for control in range(6):
    num.append(num[control] + num[control+1])
    control+=1 
print("Números:",num)