#Escreva um algoritmo para ler o número total de eleitores de um município,
# o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
def coletarPositivoInteiro():
    num = int(input())
    while(num <= 0):
        print('Erro!!! Informe um valor positivo')
        num = int(input('Informe um numero: '))
    return num

def transformarPercentual(num, total):
    percentual = (num / total) * 100
    return percentual

def eleicao():
    print('informe o total de votos brancos: ')
    brancos = coletarPositivoInteiro()
    print('informe o total de votos nulos: ')
    nulos = coletarPositivoInteiro()
    print('informe o total de votos validos: ')
    validos = coletarPositivoInteiro()
    print('informe o total de eleitores: ')
    total = coletarPositivoInteiro()
    if((brancos+nulos+validos) == total): #verificar se total é igual a brancos, validos e nulos
        pBrancos = transformarPercentual(brancos,total)
        pNulos = transformarPercentual(nulos,total)
        pValidos = transformarPercentual(validos,total)
        return 'Votos brancos:{}% \nVotos nulos:{}% \nVotos validos:{}% '.format(pBrancos,pNulos,pValidos)
    else:
        return 'Números de brancos, válidos e nulos é diferentes do total de eleitores, digite novamente!'



