from flask_restful import Resource, reqparse
from resources.teste import dadosDB


class DadosReceive(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': dadosDB}

class DadoReceive(Resource):

    def __init__(self) -> None:
        self.argumentos = reqparse.RequestParser()
        self.argumentos.add_argument('mes')
        self.argumentos.add_argument('ano')
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
        
        for dado in dadosDB:
                
            if dado['dado_id'] == dado_id:
                return dado

        return {'message': 'Dado not found'}, 404

    def post(self, dado_id):

        dados = self.argumentos.parse_args()
        novo_dado = {'dado_id': int(dado_id), **dados}

        checkDado = self.findDado(dado_id)

        if checkDado == None:
            dadosDB.append(novo_dado)
            return novo_dado, 200
        else: 
            return {'message': ' dado_id already exist'}, 403
    
    def put(self, dado_id):

        dadoInDB = self.findDado(dado_id)
        dados = self.argumentos.parse_args()
        novo_dado = {'dado_id': int(dado_id), **dados}

        if dadoInDB:           
            dadoInDB.update(novo_dado)
            return novo_dado, 200
        
        dadosDB.append(novo_dado)
        return novo_dado, 201

    def delete(self, dado_id):

        dadoInDB = self.findDado(dado_id)
        if dadoInDB:
            dadosDB = [dado for dado in dadosDB if dadosDB['dado_id'] != int(dado_id)]
            return {'message': 'Dado deleted'}
        return {'message': "dado_id not exist"}
    
    def findDado(self, dado_id):
        for dado in dadosDB:
            if dado['dado_id'] == int(dado_id):
                return dado
        return None