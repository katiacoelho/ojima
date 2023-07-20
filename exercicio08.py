#Exercicic08
#Escrever um algoritimo que leia 10 numeros inteiros e, ao final, apresente a soma de todos os numeros lidos:

def somarInteiro():
    soma = 0
    for i in range(1,11,1):
           num = int(input('{}º numero: '.format(i)))
           soma += num
    return 'A soma dos numeros digitados foi {}'.format(soma)


