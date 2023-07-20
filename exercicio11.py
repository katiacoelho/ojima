#exercicio11
#Escreva um algoritmo que leia valores inteiros e encontre o maior e o menor deles.
# Termine a leitura se o usuário digitar 0(zero).

def maiorMenor():
    maior = 0
    menor = 0
    num = 1
    flag = False #Valor lógico, binário
    while (num != 0):
        num = int(input('Informe um número: '))
        if(num !=0): #Evita-se que o zero seja relacionado
            if (flag == False):
            #primeira vez do codigo, eu instancio a variael
                 maior = num
                 menor = num
                 flag = True

            if (num > maior):
                maior = num

            if (num < menor):
                menor = num

    return 'Maior: {} \nMenor: {}'.format(maior, menor)