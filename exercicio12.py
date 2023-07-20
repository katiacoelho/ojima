#exercicio12
#Escreva um algoritm oque leia 20 valores inteiros e ao final exiba:
# A)A soma dos números positivos;
# B)A quantidade de valores negativos;

def positivoNegatico():
    soma = 0
    contarNegativo = 0 #não se pode usar (i) neste caso, pois o "i" do "for" esta contando os números
    for i in range(20):
        num = int(input('{} número: '.format(i+1)))
        # A) soma dos positivos
        if(num > 0):
            soma += num
        # B) conta os negativos
        elif(num < 0):
            contarNegativo += 1
    return 'positivos: {} \n Contar Negativos: {}'.format(soma,contarNegativo)
