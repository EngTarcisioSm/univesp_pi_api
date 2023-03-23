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
  
+ ix [22.03.2023] partição da api em duas, sendo que uma preparada para ser trabalhada em um banco de dados enquanto a outra utilizará o googlesheets como banco de dads 
  + testes de get nas duas, com dados estáticos 
