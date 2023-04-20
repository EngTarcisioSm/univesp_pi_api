import json
import requests 

from datetime import datetime
import random
import time

BASE_URL = 'http://127.0.0.1:5000'


def get(complement_get:str):
    answer_get = requests.request('GET', BASE_URL + complement_get)
    return int(answer_get.status_code), answer_get.json()

def post(complement_post:str, data:dict):
    
    header = {
        'Content-Type': 'application/json'
    }
    answer_post = requests.request('POST', BASE_URL + complement_post, json=data, headers=header)
    return int(answer_post.status_code), answer_post.json()

def created_msg():
    return {
        "ano": str(datetime.now().year),
        "mes": str(datetime.now().month),
        "dia": str(datetime.now().day),
        "hora": str(datetime.now().hour),
        "minuto": str(datetime.now().minute),
        "segundo": str(datetime.now().second),
        "milissegundos": "000",
        "corrente": str(0.5 + (random.random()))[0:4].replace(".", ","),
        "tensao": str(100 + (random.random()* 10))[0:6].replace(".", ","),
        "temperatura": str(20 + (random.random()* 5))[0:5].replace(".", ","),
        "type": "sheets"
    }

def test_post():
    ID = 2
    while True:
        complement = '/dado/'+str(ID)
        try:
            dado = created_msg()
            code, _ = post(complement, dado)

            if code == 200:
                ID = ID + 1
                log("OK " + str(ID)+ " " +str(code) +" " + str(dado))
            elif code == 403:
                log("ERROR " + str(ID)+ " " +str(code) + " " + str(dado) + "NOVA TENTATIVA")
                ID = ID + 1
            else:
                log("ERROR " + str(ID)+ " " +str(code) + " " + str(dado) + "ERRO INDETERMINADO")
        except:
            log("ERROR " + str(ID)+ " " + "ERRO INDETERMINADO")
        time.sleep(1)

def log(dado:str):
    with open("log.txt", "a") as fileLog:
        fileLog.write(dado + "\n")


if __name__ == '__main__':
    test_post()
