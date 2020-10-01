from interface.cores import *
from validação.valida import *


def linha(s, x=70, cr=0):
    '''
     => Gera uma sequencia de caracteres, por exemplo uma linha de 40 '-' de cor amarela:
     linha('-', 10, 7) // ----------
    :param s: caractere
    :param x: quantidade de da sequencia, padrão 70
    :param cr: cor, padrão 0

    '''
    print(f'{cor(cr)}{s}'*x, f'{cor(0)}')


def cabecalho(x, msg):
    '''
    => Gera um cabeçalho de titulo de tela, utiliza a função linha() e a função cor(),
      que por padrão usa a cor '11 azul claro'
    
    :param x: caractere da função linha, com padrão 70 
    :param msg: titulo da tela 
    
    '''
    linha(x, cr=11)
    print('{}{}{}'.format(cor(11), msg.center(60), cor(0)))
    linha(x, cr=11)


def menu(lst, cab):
    '''
    => Gera um menu, esta função usa uma lista com as opções desejadas.

    Ex: menu(['INCLUSÃO', 'CONSULTA', 'SAIR'], 'MENU PRINCIPAL')

    ----------------------------------------------------------------------
                       MENU PRINCIPAL
    ----------------------------------------------------------------------
    [1] INCLUSÃO [2] CONSULTA [3] SAIR

    :param lst: lista de opções
    :param cab: titulo do cabeçalho
    :return: retorna a opção desejada
    '''
    cabecalho('-', cab)
    while True:
        op = 1
        for val in lst:
            print(f'{cor(7)}[{op}] {val}{cor(0)} ', end='')
            op += 1
        print()
        linha('-', cr=9)
        resp = leiaInt(f'{cor(1)}Escolha sua opção{cor(0)} ')
        if resp > len(lst):
            print(f'{cor(3)}Opção inválida{cor(0)}')
        else:
            break
    return resp

