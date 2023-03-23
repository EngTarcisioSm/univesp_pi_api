from flask_restful import Resource
from resources.teste import dados


class DadosReceiveSheets(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': dados}   