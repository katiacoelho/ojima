#exercicio15
#Em um concurso de miss, os jurados precisam digitar o nome das 16 candidatas e suas respectivas notas (0a10).
# Crie um programa que leia estas informações e que, ao final do programa,
# apresente apenas o nome e a nota da vencedora.
def validacaoNotas():
    nota = float(input('informe uma nota: '))
    while((nota < 0) or (nota > 10)):
        print('Erro!!! Informe uma nota entre 0 e 10')
        nota = float(input('informe uma nota: '))
    return nota

def miss():
    nomeVencedora = ''
    notaVencedora = 0
    for i in range(1,17):
        nome = input('informe o nome da {} candidata: '.format(i))
        nota = validacaoNotas()#Números com virgula e não negativos

        if(nota > notaVencedora):# verificação da vencedora
            notaVencedora = nota
            nomeVencedora = nome
    return 'Vencedora: {}\nNota: {}'.format(nomeVencedora, notaVencedora)

