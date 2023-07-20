notas = []#vetor Global = Todas as funções podem visualizar/ Usar esse vetor

def preencherVetor(fim):
    for i in range(fim):
        num = int(input('Informe a {}ª nota: '.format(i+1)))
        notas.append(num) #adicionando notas no vetor

def consultarVetor(fim):
    for i in range(fim):
        print('{}ª Posição: {}'.format(i+1,notas[i]))

def apagarPosicao(posicao):
    if(len(notas) < posicao):
        print('Impossivel remover, pois o tamanho é menor que a posiçao')
    else:
        del(notas[posicao]) #Excluindo um dado do vetor
        print('Removido com sucesso!')

