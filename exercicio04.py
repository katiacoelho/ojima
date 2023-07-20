#Exercício04
#Faça um algoritmo que calcule a soma dos números inteiros de 1 a 100.
def somarInteiro():
    soma = 0
    #"i" sempre começa a contar em 0, range() pode indicar o inicio, o fim + 1 e de qto e qto ele vai rodar(intervalo), ex: (1,101, 2)
    for i in range(1,101):
        soma += i

    return 'A soma dos elementos entre 1 e 100 é: {}'.format(soma)