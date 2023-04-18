from flask_restful import Resource, reqparse
from models.dadoModel import DadoModel

from modules.moduleSheets import InterationSheets as ISheets


class FindID(Resource):

    def __init__(self):
        self.iterationSheets = ISheets()
    

    def get(self):
        dados_recieve = self.iterationSheets.getSheets('Sheet1', "A2", "E2000000")
        return {'ID': len(dados_recieve)+1}