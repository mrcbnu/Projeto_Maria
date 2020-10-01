from lib.relatorios import *
from validação.valida import *
from time import sleep


def arqExiste(arquivo):
    '''
    => Verifica se a existencia do arquivo de dados da temporada.
    :param arquivo: nome do arquivo
    :return: retorna False se o arquivo não for encontrado
             retorna True se o arquivo for encontrado
    '''
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arquivo):
    '''
    => Cria um arquivo de de dados (.txt)
    :param arquivo: nome do arquivo
    '''

    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print(f'{cor(3)}Houve um Erro na criação do arquivo!{cor(0)}')

