# Refência do Namespace validação.valida

## Funções

##### def leiaInt (msg)
 
##### def leiaFloat (msg)
 
##### def leiaData (msg)
 
##### def leiaResp (msg)
***
### leiaInt(msg)

Função que valida a entrada de um numero inteiro.

__parametro msg:__ indicação ao usuario informando a entrada do valor a ser validado

__return:__ retorna o valor correto

```
 def leiaInt(msg):
     
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
```  
  
### leiaFloat()

Função que valida a entrada de um numero real.

__parametro msg:__ indicação ao usuario informando a entrada do valor a ser validado

__return:__ retorna o valor correto

```
 def leiaFloat(msg):
     
     while True:
         try:
             num = float(input(msg))
         except (TypeError, ValueError):
             print(f'{cor(3)}não é um numero real valido!{cor(0)}')
             continue
         else:
             return num
``` 
 ### leiaData(msg)
Função que recebe a data informada pelo usuario e retorna a correta.

__parametro msg:__ mensagem informando o usuario a dar entrada no valor

__return:__ retorna a data correta

 ```
 def leiaData(msg) 
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
```   

### leiaResp(msg)

Função que valida a resposta 'S'(sim) ou 'N'(não) a uma determinada pergunta.

__parametro msg:__ indicação ao usuario informando a entrada da resposta esperada

__return:__ resposta correta

```
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
```
