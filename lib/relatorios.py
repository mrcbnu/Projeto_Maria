from lib.cadastros import *
from interface.layout import *
from interface.cores import *
from time import sleep
from datetime import *

def tabela(msg):
    '''
    => Gera um cabeçalho de titulos das tabelas de consulta.
    :param msg: título da tabela
    '''
    print(f'{cor(1)}{msg:^69}')
    linha('-', 69)
    print('|        |          |  Mínimo   |  Máximo   | Quebra de | Quebra de |')
    print('| Jogo   |  Pontos  |    da     |    da     |  record   |  record   |')
    print('|        |          | temporada | temporada |  Mínimo   |  Máximo   |')
    linha('-', 69)


def tabelaParcial(arq, ini, fim):
    '''
    => Exibe os dados conforme a indicação do usuário.
    :param arq: arquivo onde estão listados as jogos e as estatisticas da temporada.
    :param ini: rodada inicial
    :param fim: rodada final
    '''
    try:
        arq_par = open(arq, 'r')
    except:
        print(f'{cor(3)} Erro ao acessar o arquivo {arq}!{cor(0)}')
    else:
        tabela('TABELA PARCIAL')
        for v, r in enumerate(arq_par):
            campo = r.split(';')
            campo[5] = campo[5].replace('\n', '')
            campo[0] = int(campo[0])
            if ini <= campo[0] <= fim:
                if v % 2 == 0:
                    c = cor(1)
                else:
                    c = cor(2)
                f = cor(0)
                print(f'|{c}{campo[0]:^8}{f} {c}{campo[1]:^10}{f} {c}{campo[2]:^11}{f} '
                      f'{c}{campo[3]:^11}{f} {c}{campo[4]:^11}{f} {c}{campo[5]:^11}{f}|')
        linha('-', 69)
        arq_par.close()


def tabelaGeral(arq):
    '''
    => Exibe todos os dados da temporada.
    :param arq: arquivo onde estão listados as jogos e as estatisticas da temporada.

    '''
    try:
        arq_ger = open(arq, 'r')
    except:
        print(f'{cor(3)} Erro ao acessar o arquivo {arq}!{cor(0)}')
    else:
        print(f'{cor(5)}Analizando os campos .', end='')
        sleep(0.25)
        print(' .', end=''); sleep(0.25); print(' .', end=''); sleep(0.25)
        print(' .', end=''); sleep(0.25); print(f' tudo certo! ', end=''); sleep(0.25)
        print(f'{cor(1)}Gerando a tabela {cor(0)}\n')
        sleep(0.50)
        tabela('TABELA GERAL')
        for v, r in enumerate(arq_ger):
            campo = r.split(';')
            campo[5] = campo[5].replace('\n', '')
            if v % 2 == 0:
                c = cor(1)
            else:
                c = cor(2)
            f = cor(0)
            print(f'|{c}{campo[0]:^8}{f} {c}{campo[1]:^10}{f} {c}{campo[2]:^11}{f} '
                  f'{c}{campo[3]:^11}{f} {c}{campo[4]:^11}{f} {c}{campo[5]:^11}{f}|')
        linha('-', 69)
        arq_ger.close()


def resumoGeral(arq):
    '''
    => Gera um resumo dos dados coletados durante a temporada:
        - Jogos disputados;
        - soma dos pontos;
        - média de pontos por partida;
        - maior pontuação;
        - jogo onde fez a maior pontuação, se for mais de um jogo, será apresentado o primeiro;
        - menor pontuação;
        - jogo onde fez a menor pontuação, se for mais de um jogo, será apresentado o primeiro.

    :param arq: arquivo oonde está armazendado os dados da temporada.

    '''
    try:
        arq_res = open(arq, 'r')
    except:
        print(f'{cor(3)} Erro ao acessar o arquivo {arq}!{cor(0)}')
    else:
        qdadeJogos = contaJogos(arq)
        qdadePontos = mediaPontos = 0
        for v, r in enumerate(arq_res):
            campo = r.split(';')
            campo[5] = campo[5].replace('\n', '')
            pontos = int(campo[1])
            qdadePontos += pontos
            if v == 0:
                min = max = pontos
            if pontos <= min:
                min = pontos
                jogoRecMim = campo[0]
            if pontos >= max:
                max = pontos
                jogoRecMax = campo[0]

        mediaPontos = round(qdadePontos/qdadeJogos, 2)
        print()
        print('{}{:^46}{}\n'.format(cor(7), 'ESTATÍSTICA DO JOGADOR', cor(0)))
        print(f' -> JOGOS DISPUTADOS....................: {qdadeJogos:>5}')
        print(f' -> PONTOS MARCADOS.....................: {qdadePontos:>5}')
        print(f' -> MÉDIA DE PONTOS POR PARTIDA.........: {mediaPontos:>3}')
        print(f' -> MENOR PONTUAÇÃO.....................: {min:>5}')
        print(f'   -> JOGO EM QUE MARCOU MENOS PONTOS...: {jogoRecMim:>4}º')
        print(f' -> MAIOR PONTUAÇÃO.....................: {max:>5}')
        print(f'  -> JOGO EM QUE MARCOU MAIS PONTOS.....: {jogoRecMax:>4}º')
        print()
        linha('-')

