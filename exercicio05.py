#Exercicio05
#Construa um programa que exiba a tabuada de 1 até N.
def tabuada(num, n):
    for i in range(1, n+1):
        print('{} * {} = {}'.format(num,i,num * i))

def coletarPositivo():
    num = float(input('informe um número: '))
    while(num <= 0):
        print('Erro! informe um número: ')
        num = int(input('informe um número: '))
    return num
