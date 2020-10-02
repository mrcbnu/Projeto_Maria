![MARIA V1.0](https://github.com/mrcbnu/Projeto_Maria/blob/master/html/LOGO%20MARIA.png)

# Apresentação

Este aplicativo tem como função principal registar a pontuação de uma jogadora de basquete, **MARIA**, e com base nesses pontos, gerar uma serie de dados estatísticos.

O programa funciona em modo terminal e tem 2 menus de opções.

#### MENU PRINCIPAL
***
#### [1] INCLUSÃO [2] CONSULTA [3] SAIR

* A opção [1] INCLUSÃO, abre a interface de entrada de pontos que Maria marcou em uma partida.

* A opção [2] CONSULTA, abre outro menu com 4 opções;

* A opção [3] SAIR, encerra o programa.

#### MENU CONSULTA
***
#### [1] TABELA GERAL [2] TABELA PARCIAL [3] RESUMO [4] VOLTAR

* A opção [1] TABELA GERAL, gera uma tabela com todos os dados processados a partir dos pontos de cada partida;

* A opção [2] TABELA PARCIAL, gera uma tabela listando dados de partidas especificas;

* A opção [3] RESUMO, gera um relatório contendo um resumo do desempenho de Maria, total de partidas, total de pontos, média de pontos por partida, maior pontução e em qual partida e menor pontução e em qual partida.

* A opção [4] VOLTAR, volta para o menu principal.

# Documentação

## Pacotes

Esta é a lista com os pacotes e suas respectivas descrições:

 * __interface__	
   * cores	
   * layout	
 * __lib__	
   * arquivo	
   * cadastros	
   * relatorios	
  * __main__	
 * __validação__	
   * valida	

## Refência do Namespace interface.cores
# Funções
__def	cor(x)__

Função que gera um codigo de cores no padrão escape sequence ANSI.

:param x: numero de posição do codigo ANSI na tupla cores.

:return: retorna o codigo da cor.

 
 ``` 
 def cor(x): 
 
     cores = (
     
         '\033[m',        # 0 - sem cor
         '\033[1;30m',    # 1 - branco
         '\033[1;7;30m',  # 2 - branco_in
         '\033[1;31m',    # 3 - vermelho
         '\033[1;30;41m', # 4 - vermelho_in
         '\033[1;32m',    # 5 - verde
         '\033[1;7;32m',  # 6 - verde_in
         '\033[1;33m',    # 7 - amarelo
         '\033[1;7;33m',  # 8 - amarelo_in
         '\033[1;34m',    # 9 - azul
         '\033[1;35m',    # 10 - roxo
         '\033[1;36m',    # 11 - azulc
         '\033[1;7;36m',  # 12 - azul_in
         '\033[1;37m'     # 13 - cinza
         )
  
     for n, v in enumerate(cores):
         if x == n:
             return v
```
  
