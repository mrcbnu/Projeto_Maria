# Refência do Namespace interface.layout
## Funções
### def	cabecalho(s, x=70, cr=0)

Gera um cabeçalho de titulo de tela, utiliza a função linha() e a função cor(),
que por padrão usa a cor '11 azul claro'

__parametro x:__ caractere da função linha, com padrão 70 

__parametro msg:__ titulo da tela 
 ```
 def cabecalho(x, msg):
     linha(x, cr=11)
     print('{}{}{}'.format(cor(11), msg.center(60), cor(0)))
     linha(x, cr=11)
```

### def linha(x, cr=0)

Gera uma sequencia de caracteres, 

por exemplo uma linha de 10 '-' de cor amarela:
```
 linha('-', 10, 7) // ----------
```
__parametro s:__ caractere

__parametro x:__ quantidade de da sequencia, padrão 70

__parametro cr:__ cor, padrão 0
```
def linha(x, cr=0)
  print(f'{cor(cr)}{s}'*x, f'{cor(0)}')
```
 
### def menu(lst, cab)
 
Gera um menu, esta função usa uma lista com as opções desejadas.

Ex: 
```
menu(['INCLUSÃO', 'CONSULTA', 'SAIR'], 'MENU PRINCIPAL')
```
Resultado:
```
----------------------------------------------------------------------
                   MENU PRINCIPAL
----------------------------------------------------------------------
[1] INCLUSÃO [2] CONSULTA [3] SAIR
```

__parametro lst:__ lista de opções

__parametro cab:__ titulo do cabeçalho

__return:__ retorna a opção desejada
```
 def menu(lst, cab):     
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
 ```
# Refência do Namespace interface.cores

## Funções

### def	cor(x)

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
   
