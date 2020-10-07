# Refência do Namespace lib.arquivo
## Funções
##### def	arqExiste (arquivo)
 
##### def criarArquivo (arquivo)
***
### def arqExiste (arquivo) 
Verifica se a existencia do arquivo de dados da temporada.

__parametro arquivo:__ nome do arquivo

__return:__ retorna False se o arquivo não for encontrado, retorna True se o arquivo for encontrado

``` 
 def arqExiste(arquivo):
          try:
         a = open(arquivo, 'rt')
         a.close()
     except FileNotFoundError:
         return False
     else:
         return True
```

### def criarArquivo(arquivo)

Cria um arquivo de dados (.txt)

__parametro arquivo:__ nome do arquivo
 
 ```
 def criarArquivo(arquivo):
       
     try:
         a = open(arquivo, 'wt+')
         a.close()
     except:
         print(f'{cor(3)}Houve um Erro na criação do arquivo!{cor(0)}')
 ```
# Refência do Namespace lib.cadastros
## Funções
##### def inclusao (msg)
 
##### def registraDados (arq, pontos)
 
##### def contaJogos (arq)
*** 
### inclusao()
	
Entrada da pontuação da partida, essa função aceita somente numeros inteiros
entre 0 e 1000.
__parametro msg:__ mensagem de solicitação de entrada de dados

__return:__ valor inserido pelo usuário
 
 ```
 def inclusao(msg):
     
     while True:
         pontos = leiaInt(msg)
         if pontos < 0 or pontos > 1000:
             print('Placar inválido, entre com valor entre 0 e 1000')
         else:
             break
  
     return pontos
 ``` 
  
### registraDados()

Função que recebe o valor retornado da função inclusao(), processando e gravando os dados com base nesse valor.

estrutura do arquivo de dados (.txt):
```
jogo; pontos; minimo; maximo; record min; record max
```
__param arq:__ arquivo de armazenagem dos dados processados

__param pontos:__ valor retornado da função inclusao()

```
 def registraDados(arq, pontos):
     
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
```  
  
### contaJogos()
Função que conta a quantidade de jogos registrados no arquivo

__parametro arq:__ arquivo de dados

__return:__ número de jogos
 
 ```
 def contaJogos(arq):
     
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
```
# Referência do Namespace lib.relatorios
## Funções
##### def tabela (msg)
 
##### def tabelaParcial (arq, ini, fim)
 
##### def tabelaGeral (arq)
 
##### def resumoGeral (arq)

*****
### tabela(msg)
Gera um cabeçalho de titulos das tabelas de consulta.

__param msg:__ título da tabela

```
 def tabela(msg):
     
     print(f'{cor(1)}{msg:^69}')
     linha('-', 69)
     print('|        |          |  Mínimo   |  Máximo   | Quebra de | Quebra de |')
     print('| Jogo   |  Pontos  |    da     |    da     |  record   |  record   |')
     print('|        |          | temporada | temporada |  Mínimo   |  Máximo   |')
     linha('-', 69)
```
### tabelaParcial(arq, ini, fim)
	
Exibe os dados conforme a indicação do usuário.
__parametro arq:__ arquivo onde estão listados as jogos e as estatisticas da temporada.

__parametro ini:__ rodada inicial

__parametro fim:__ rodada final
 
 ```
 def tabelaParcial(arq, ini, fim):
     
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
 ```  

### tabelaGeral(arq)
	
Exibe todos os dados da temporada em uma tabela.

__parametro arq:__ arquivo onde estão listados as jogos e as estatisticas da temporada.
 
```
 def tabelaGeral(arq):
     
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
``` 
  


### resumoGeral(arq)

Gera um resumo dos dados coletados durante a temporada:

 * Jogos disputados;    
 * soma dos pontos;    
 * média de pontos por partida;    
 * maior pontuação;    
 * jogo onde fez a maior pontuação, se for mais de um jogo, será apresentado o primeiro;
 * menor pontuação;
 * jogo onde fez a menor pontuação, se for mais de um jogo, será apresentado o primeiro.

__param arq:__ arquivo oonde está armazendado os dados da temporada.
 
 ```
 def resumoGeral(arq):
     
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
 ``` 
  