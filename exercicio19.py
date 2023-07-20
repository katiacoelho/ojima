#Escreva um programa para informar o maior elemento de um vetor de 5 posições do tipo inteiro
elementos = []

def preencherElemento(fim):
    for i in range(fim):
        num = int(input('Informe o {}º elemento: '.format(i+1)))
        elementos.append(num)

def consutarElemento(fim):
    for i in range(fim):
        print('{}º Posição: {}'.format(i+1,elementos[i]))

def maiorElemento
