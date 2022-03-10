'''
QUESTÃO 10.Escreva um programa que leia n números e mostre a soma dos mesmos. 
O programa deve parar de ler quando o usuário digitar -1.
'''
n=0
soma=0
while n !=-1:
    n=int(input("Digite um número"))
    if n == -1:
        break
    else:
        soma = soma+n
print(f"A soma dos números é: {soma}")