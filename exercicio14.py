#exercicio14
#Escreva um programa que leia um valor correspondente a o número de jogadores de um time de vôlei.
# O programa deverá ler uma altura para cada um dos jogadores e, ao final, informar a altura média do time.

from exercicio05 import coletarPositivo

def mediaVolei():
    soma = 0
    qtde = int(input('informne a quantidade de pessoas no time: '))

    for i in range(qtde): #coletar todas as alturas
        altura = coletarPositivo()
        soma += altura
    return 'A altura média do time é {}' .format(soma/qtde)

