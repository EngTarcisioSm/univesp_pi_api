# PASSOS DA CRIACAO DA API-REST DO ROJETO INTEGRADOR UNIVESP

## OBSERVAÇÕES 
+ Linguagem utilizada:
  + Python
+ Framework:
  + Flask
+ SO utilizado para desenvolvimento 
  + Ubuntu 22.04

## Passos 

+ i.    criar o ambiente virtual
  + Instalação da biblioteca de criação de ambiente virtual 
    ~~~bash
        $ apt install python3.10-venv
    ~~~
  + Criacao do ambiente virtual:
    ~~~bash
        $ python3 -m venv venv
    ~~~
+ ii.   instalação do framework flask e flask_restful 
    ~~~bash
        $ pip install flask && pip pip install flask-restful
    ~~~
+ iii.  geração de arquivo requirements.txt [recorrente]
    ~~~bash
        $ pip freeze > requirements.txt
    ~~~
+ iv.   inicializando o projeto
+ v.    iniciallização do ambiente virtual
    ~~~
        $ source venv/bin/activate
    ~~~
+ vi.   criando o repositorio git 
    ~~~
        $ git init 
    ~~~
+ vii.  criando o arquivo gitgnore
    ~~~
        $ touch .gitgnore 
    ~~~
+ viii. criando o repositório no github
  

