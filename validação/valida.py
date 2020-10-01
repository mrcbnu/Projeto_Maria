from interface.cores import *
from datetime import *


def leiaInt(msg):
    '''
    -> Função que valida a entrada de um numero inteiro
    :param msg: indicação ao usuario informando a entrada do valor a ser validado
    :return: retorna o valor correto
    '''
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print(f'{cor(3)}não é um numero inteiro valido!{cor(0)}')
            continue
        except KeyboardInterrupt:
            print(f'{cor(5)}O usuário preferiu não informar o valor {cor(0)}')
            return 0
        else:
            return num


def leiaFloat(msg):
    '''
    -> Função que valida a entrada de um numero real
    :param msg: indicação ao usuario informando a entrada do valor a ser validado
    :return: retorna o valor correto
    '''
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print(f'{cor(3)}não é um numero real valido!{cor(0)}')
            continue
        else:
            return num


def leiaData(msg) -> object:
    data = ''
    while True:
        try:
            data = str(input(msg))
            data = datetime.strptime(data, '%d/%m/%Y')
        except:
            print(f'{cor(3)}Data errada{cor(0)}')
        else:
            break
    return data

def leiaResp(msg):

    while True:
        resp = str(input(msg)).upper().strip()
        if resp == 'S':
            resp = True
            break
        elif resp == 'N':
            resp = False
            break
        else:
            print('Opçao inválida...')
    return resp

