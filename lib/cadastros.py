from interface.layout import *
from lib.arquivo import *


def inclusao(msg):
    '''
    => Entrada da pontuação da partida, essa função aceita somente numeros inteiros
    entre 0 e 1000.
    :param msg: Pergunta de entrada de dados
    :return: valor inserido pelo usuário
    '''

    while True:
        pontos = leiaInt(msg)
        if pontos < 0 or pontos > 1000:
            print('Placar inválido, entre com valor entre 0 e 1000')
        else:
            break

    return pontos


def registraDados(arq, pontos):
    '''
    => Função que recebe o valor retornado da função inclusao()
       processando e gravando os dados com base nesse valor:
       estrutura do arquivo de dados (.txt)

       jogo; pontos; minimo; maximo; record min; record max

    :param arq: arquivo de armazenagem dos dados processados
    :param pontos: valor retornado da função inclusao)
    :return:
    '''

    with open(arq, 'r') as novo:
        for reg in novo:
            ult_reg = reg.split(';')
    jogo = (int(ult_reg[0]) + 1)
    min = int(ult_reg[2])
    max = int(ult_reg[3])
    r_min = int(ult_reg[4])
    r_max = int(ult_reg[5])

    if pontos < min:
        min = pontos
        r_min += 1
    if pontos > max:
        max = pontos
        r_max += 1
    arq_jogo = open(arq, 'at')
    try:
        arq_jogo.write(f'{jogo};{pontos};{min};{max};{r_min};{r_max}\n')
        print(f'{cor(9)}Registrado!{cor(0)}')
        arq_jogo.close()
    except:
        print(f'{cor (3)}Problemas em gravar os dados!{cor (0)}')


def contaJogos(arq):
    '''
    => Função que conta a quantidade de jogos registrados no arquivo
    :param arq: arquivo de dados
    :return: número de jogos
    '''
    arq_parcial = open(arq, 'r')
    cont = 0
    while True:
        jogos = arq_parcial.readline()
        cont += 1
        if jogos == '':
            cont -= 1
            break
    arq_parcial.close()
    return cont

