from interface.cores import *
from interface.layout import *
from interface.vinheta import *
from lib.relatorios import *
from validação.valida import *
from lib.cadastros import *
from lib.arquivo import *
import os


def main():
    os.system('cls')
    abertura()
    arq = 'jogos.txt'

    print('')

    while True:
        os.system('cls')
        cabecalho('-', 'MARIA v1.0')
        opção = menu(['INCLUSÃO', 'CONSULTA', 'SAIR'], 'MENU PRINCIPAL')
        if opção == 1:
            cabecalho('-','INCLUSÃO')
            while True:
                with open(arq, 'r') as novo:
                    for reg in novo:
                        ult_reg = reg.split(';')
                        proximo = int(ult_reg[0]) + 1
                pontos = inclusao(f'Pontos marcados no {proximo}º jogo: ')
                registraDados(arq, pontos)
                continua = leiaResp('Deseja incluir outro jogo [S/N]: ')

                if not continua:
                    break
                linha('-')

        elif opção == 2:
            while True:
                os.system('cls')
                cabecalho('-', 'MARIA v1.0')
                op_1 = menu(['TABELA GERAL', 'TABELA PARCIAL', 'RESUMO', 'VOLTAR'], 'CONSULTA')
                if op_1 == 1:
                    while True:
                        existe = arqExiste(arq)
                        if not existe:
                            print(f'{cor(3)}Não há registro de jogos!{cor(0)}')
                            break
                        else:
                            print('{}{:^19}{}'.format(cor(2), 'TABELA GERAL', cor(0)))
                            linha('-')
                            tabelaGeral(arq)
                            input()
                            break
                elif op_1 == 2:
                    while True:
                        existe = arqExiste(arq)
                        if not existe:
                            print(f'{cor (3)}Não há registro de jogos!{cor (0)}')
                            break
                        else:
                            jogos = contaJogos(arq)
                            print('{}{:^19}{}'.format(cor(2), 'TABELA PARCIAL', cor(0)))
                            linha('-')
                            while True:
                                ini = leiaInt('Rodada inicial: ')
                                if ini <= 0 or ini > jogos:
                                    print(f'{cor(3)}Rodada incorreta ou inexistente... Tente novamente{cor(0)}')
                                else:
                                    break
                            while True:
                                fim = leiaInt('Rodada final: ')
                                if fim <= 0 or fim > jogos:
                                    print(f'{cor(3)}Rodada incorreta ou inexistente... Tente novamente{cor(0)}')
                                elif fim < ini:
                                    print(f'{cor(3)}Rodada final não pode ser inferior que rodada inicial{cor(0)}')
                                else:
                                    break
                            tabelaParcial(arq, ini, fim)
                            input()
                        break
                elif op_1 == 3:
                    while True:
                        existe = arqExiste(arq)
                        if not existe:
                            print(f'{cor(3)}Não há registro de jogos!{cor(0)}')
                            break
                        else:
                            print('{}{:^19}{}'.format(cor(2), 'RESUMO', cor(0)))
                            linha('-')
                            resumoGeral(arq)
                            input()
                            os.system('cls')
                            break

                elif op_1 == 4:
                    break
                else:
                    print('opção errada')
        elif opção == 3:
            print('\nEncerrando... \n')
            sleep(2)
            print('ATÉ LOGO!')
            break
        else:
            print('opção errada')


if __name__ == '__main__':
    main()
