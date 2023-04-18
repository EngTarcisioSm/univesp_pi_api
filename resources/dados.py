from flask_restful import Resource, reqparse
from models.dadoModel import DadoModel

from modules.moduleSheets import InterationSheets as ISheets

iterationSheets = ISheets()

def organizeReqGet(dado_id, data:str):
    quebra_geral = data.split(" ")              # [0] data full, [1] hora full, [2] tensao [3] corrente [4] temperatura 
    quebra_data = quebra_geral[0].split("/")    # [0]: dia [1]:mes [2]ano 
    quebra_hora = quebra_geral[1].split(":")    # [0]: hora [1]:minuto [2]segundo

    return {
        "ano": quebra_data[2],
        "mes": quebra_data[1],
        "dia": quebra_data[0],
        "hora": quebra_hora[0],
        "minuto": quebra_hora[1],
        "segundo": quebra_hora[2],
        "milissegundos": "000",
        "corrente": quebra_geral[3],
        "tensao": quebra_geral[2],
        "temperatura": quebra_geral[4],
        "type": "sheets"
    }

def generateJson(dado_id, ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type='db'):
    novo_dado_obj = DadoModel(int(dado_id), ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type)
    return novo_dado_obj.json()

class DadosReceive(Resource):
    # implementacao de metodo get para teste
    def get(self):
        ...
        dados_recieve = iterationSheets.getSheets('Sheet1', "A2", "E2000000")
        id = 2
        answer = list()
        for data in dados_recieve:
            data_str = data[0] + " " + data[1] + " " + data[2] + " " + data[3] + " " + data[4]
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
        
        if(dado_id == 0 or dado_id == 1):
            return {'message': 'Unauthorized'}
        
        data = self.findDado_sheets(dado_id)
        if len(data) == 0:
            return {'message': 'Dado not found'}, 404

        data_str = data[0][0] + " " + data[0][1] + " " + data[0][2] + " " + data[0][3] + " " + data[0][4]

        genetate_json = organizeReqGet(dado_id, data_str)
        
        return genetate_json

    def post(self, dado_id):

        if(dado_id == 0 or dado_id == 1):
            return {'message': 'Unauthorized'}
        
        dados = self.argumentos.parse_args()
        # dado configurado para sheets
        novo_dato_sheet = self.generateSheets(int(dado_id), **dados)
        # verifica se o endereço de ID solicitado ja contem alguma mensagem 
        if len(self.findDado_sheets(dado_id)) == 0:
            # efetuando a escrita
            iterationSheets.putSheet('Sheet1', "A" + str(dado_id), novo_dato_sheet)
            return generateJson(dado_id, **dados), 200
        else: 
            return {'message': ' dado_id already exist'}, 403
    
    def put(self, dado_id):
        
        if(dado_id == 0 or dado_id == 1):
            return {'message': 'Unauthorized'}
        
        dados = self.argumentos.parse_args()
        # dado configurado para sheets
        novo_dato_sheet = self.generateSheets(int(dado_id), **dados)

        # efetuando a escrita ou atualização
        iterationSheets.putSheet('Sheet1', "A" + str(dado_id), novo_dato_sheet)
        return generateJson(dado_id, **dados), 201
    

    def delete(self, dado_id):

        if(dado_id == 0 or dado_id == 1):
            return {'message': 'Unauthorized'}
        
        if len(self.findDado_sheets(dado_id)) == 0:
            return {'message': "dado_id not exist"}
        # deleção
        iterationSheets.putSheet('Sheet1', "A" + str(dado_id), [["", "", "", "", ""],])
        return {'message': 'Dado deleted'}
    
    
    def findDado_sheets(self, dado_id):
        return iterationSheets.getSheets(
            'Sheet1', 
            "A"+str(dado_id), 
            "E"+str(dado_id)
        )  
    
    # organizando os dados para sheets
    def generateSheets(self, dado_id, ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type):
        novo_dado_obj = DadoModel(int(dado_id), ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type)
        return novo_dado_obj.dataSendSheets()
    



