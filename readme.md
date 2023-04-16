# PASSOS DA CRIACAO DA API-REST DO ROJETO INTEGRADOR UNIVESP

## OBSERVAÇÕES 
+ Linguagem utilizada:
  + Python
+ Framework:
  + Flask
+ SO utilizado para desenvolvimento 
  + Ubuntu 22.04

## Passos 

+ i.    [20.03.2023] criar o ambiente virtual    
  + Instalação da biblioteca de criação de ambiente virtual 
    ~~~bash
        $ apt install python3.10-venv
    ~~~
  + Criacao do ambiente virtual:
    ~~~bash
        $ python3 -m venv venv
    ~~~
+ ii.   [20.03.2023] instalação do framework flask e flask_restful 
    ~~~bash
        $ pip install flask && pip pip install flask-restful
    ~~~
+ iii.  [20.03.2023] geração de arquivo requirements.txt [recorrente]
    ~~~bash
        $ pip freeze > requirements.txt
    ~~~
+ iv.   [20.03.2023] inicializando o projeto
+ v.    [20.03.2023] iniciallização do ambiente virtual
    ~~~
        $ source venv/bin/activate
    ~~~
+ vi.   [20.03.2023] criando o repositorio git 
    ~~~
        $ git init 
    ~~~
+ vii.  [20.03.2023] criando o arquivo gitgnore
    ~~~
        $ touch .gitgnore 
    ~~~
+ viii. [20.03.2023] criando o repositório no github
  
+ ix    [22.03.2023] partição da api em duas, sendo que uma preparada para ser trabalhada em um banco de dados enquanto a outra utilizará o googlesheets como banco de dads 
  + testes de get nas duas, com dados estáticos 

+ x.    [22.03.2023] refatoração do código 
  + branch 0001

+ xi.   [22.03.2023] Insersão de dados como ano, mes, dia, hora, minuto, segundo, milissegundos

+ xii.  [22.03.2023] Criação de novo método 
  + novo get para visualizar dado isolado pelo dado_id
  + criação do método post 

+ xiii. [22.03.2023] Alterada a logica de criação da apí
  + No campo de dados foi incluido mais um dado  'type', indicando se o mesmo irá para o banco de dados sql ou para o sheets, 'db' para dados e 'sheet' para google sheet, esse campo type receberá apenas esses dois valores possiveis 

+ xiv.  [27.03.2023] Inserção do metodo put
  
+ xv.   [27.03.2023] Refatoração de código 

+ xvi.   [27.03.2023] inserção da checagem em post se o id utilizado ja esta sendo utilizado

+ xvii.  [27.03.2023] Não é mais necessário no json de envio inserir o dado_id entretando na html de envio ele deve constar, exemplo:
~~~
    http://127.0.0.1:5000/dado/5
~~~
  
+ xviii. [27.03.2023] metodo delete implementado, verifica se o dado que deseja ser deletado exist.

+ xix.   [27.03.2023] inicio do processo de construção do banco de dados (modo desenvolvimento)

+ xvi.   [27.03.2023] criado o modelo para os dados 

+ xvii.  [27.03.2023] Correção de dados armazenados, os mesmos estavam sendo armazenados em tipo str, passando para tipo int e float quando necessário

+ xviii. [27.03.2023] merge de atualização no projeto efetuado 

+ xix    [14.04.2023] Criação do modulo de integração api google (drive + sheets) com api do projeto univesp no arquivo modules/moduleSheets.py

+ xx     [16.04.2023] Efetuada a integração api-Projeto-Integrador com modulo de comunicação api-google
  + metodos
    + "get geral"
    + get
    + post
    + put
    + delete

+ xxi    [16.04.2023] A inserção de dados na api-projeto-integrador deve OBRIGATÓRIAMENTE obedecer a algumas regras, do contrário o comportamento não será como aquele previsto 
  + todos os dados de entrada bem como sua chaves devem ser do tipo string 
  + ano deve ser composto por 4 caracteres sendo do tipo string
  + mes deve sempre ser composto por 2 caracteres sendo do tipo string (ex: "01" "12")
  + dia deve sempre ser composto por 2 caracteres sendo do tipo string (ex: "01" "12")
  + hora deve sempre ser composto por 2 caracteres sendo do tipo string (ex: "01" "12")
  + minuto deve sempre ser composto por 2 caracteres sendo do tipo string (ex: "01" "12")
  + segundo deve sempre ser composto por 2 caracteres sendo do tipo string (ex: "01" "12")
  + milissegundos deve sempre ser composto por 3 caracteres sendo do tipo string (ex: "001" "012" "900")
  + corrente deve sempre ser composto por 7 caracteres sendo do tipo string (ex: "001.000" "010.001" 100.000)
  + tensão deve sempre ser composto por 7 caracteres sendo do tipo string (ex: "001.000" "010.001" 100.000)
  + temperatura deve sempre ser composto por 7 caracteres sendo do tipo string (ex: "001.000" "010.001" 100.000)


- to be continue

