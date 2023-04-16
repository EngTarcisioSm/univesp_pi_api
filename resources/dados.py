from flask_restful import Resource, reqparse
from models.dadoModel import DadoModel

from modules.moduleSheets import InterationSheets as ISheets
import re

iterationSheets = ISheets()

def organizeReqGet(dado_id, data:str):
    pattern = r"(\d{2})/(\d{2})/(\d{4})-(\d{2}):(\d{2}):(\d{2}):(\d{3})\sU:(\d+\.\d+)\|I:(\d{3}\.\d+)\|T:(\d+\.\d+)"

    # Encontrar as correspondências
    matches = re.match(pattern, data)

    return generateJson(
        dado_id, 
        matches.group(3), # ano
        matches.group(2), # mes
        matches.group(1), # dia
        matches.group(4), # hora
        matches.group(5), # minuto
        matches.group(6), # segundo
        matches.group(7), # milissegundo
        matches.group(9), # corrente
        matches.group(8), # voltagem
        matches.group(10) # temperatura
    )

def generateJson(dado_id, ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type='db'):
    novo_dado_obj = DadoModel(int(dado_id), ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type)
    return novo_dado_obj.json()

class DadosReceive(Resource):
    # implementacao de metodo get para teste
    def get(self):
        dados_recieve = iterationSheets.getSheets('Sheet1', "A1", "B250000")
        id = 1
        answer = list()
        for data in dados_recieve:
            data_str = data[0] + " " + data[1]
            genetate_json = organizeReqGet(id, data_str)
            id = id + 1
            answer.append(genetate_json) 

        return {'Data': answer}


class DadoReceive(Resource):

    def __init__(self) -> None:
        self.argumentos = reqparse.RequestParser()
        self.argumentos.add_argument('ano')
        self.argumentos.add_argument('mes')
        self.argumentos.add_argument('dia')
        self.argumentos.add_argument('hora')
        self.argumentos.add_argument('minuto')
        self.argumentos.add_argument('segundo')
        self.argumentos.add_argument('milissegundos')
        self.argumentos.add_argument('corrente')
        self.argumentos.add_argument('tensao')
        self.argumentos.add_argument('temperatura')
        self.argumentos.add_argument('type')

        

    def get(self, dado_id):
        
        data = self.findDado_sheets(dado_id)
        if len(data) == 0:
            return {'message': 'Dado not found'}, 404

        data_str = data[0][0] + " " + data[0][1]
        genetate_json = organizeReqGet(dado_id, data_str)
        return genetate_json

    def post(self, dado_id):
        dados = self.argumentos.parse_args()
        # dado configurado para sheets
        novo_dato_sheet = self.generateSheets(int(dado_id), **dados)
        # verifica se o endereço de ID solicitado ja contem alguma mensagem 
        if len(self.findDado_sheets(dado_id)) == 0:
            # efetuando a escrita
            iterationSheets.putSheet('Sheet1', "A" + str(dado_id), novo_dato_sheet)
            return generateJson(int(dado_id), **dados), 200
        else: 
            return {'message': ' dado_id already exist'}, 403
    
    def put(self, dado_id):

        dados = self.argumentos.parse_args()
        # dado configurado para sheets
        novo_dato_sheet = self.generateSheets(int(dado_id), **dados)

        # efetuando a escrita ou atualização
        iterationSheets.putSheet('Sheet1', "A" + str(dado_id), novo_dato_sheet)
        return generateJson(int(dado_id), **dados), 201
    

    def delete(self, dado_id):
        if len(self.findDado_sheets(dado_id)) == 0:
            return {'message': "dado_id not exist"}
        # deleção
        iterationSheets.putSheet('Sheet1', "A" + str(dado_id), [["", ""],])
        return {'message': 'Dado deleted'}
    
    
    def findDado_sheets(self, dado_id):
        return iterationSheets.getSheets(
            'Sheet1', 
            "A"+str(dado_id), 
            "B"+str(dado_id)
        )  
    
    # organizando os dados para sheets
    def generateSheets(self, dado_id, ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type):
        novo_dado_obj = DadoModel(int(dado_id), ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type)
        return novo_dado_obj.dataSendSheets()
    



