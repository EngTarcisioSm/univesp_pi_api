# import de bibliotecas necessárias 
from flask import Flask
from flask_restful import Resource, Api

from resources.dadosDB import DadosReceiveDB
from resources.dadosSHEET import DadosReceiveSheets

# criação dos objetos 
app = Flask(__name__)
api = Api(app)

# adicionando recurso na api
api.add_resource(DadosReceiveDB, '/dados_db')
api.add_resource(DadosReceiveSheets, '/dados_sheet')


if __name__ == "__main__":

    print("Begin!!!")
    # execucao da api em modo debug
    app.run(debug=True)
