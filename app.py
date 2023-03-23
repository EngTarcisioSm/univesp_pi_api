# import de bibliotecas necessárias 
from flask import Flask
from flask_restful import Resource, Api

# criação dos objetos 
app = Flask(__name__)
api = Api(app)


class DadosReceiveDB(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': 'Corrente, tensao e temperatura'}

class DadosReceiveSheets(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': 'Corrente, tensao e temperatura'}   

# adicionando recurso na api
api.add_resource(DadosReceiveDB, '/dados_db')
api.add_resource(DadosReceiveSheets, '/dados_sheet')


if __name__ == "__main__":

    print("Begin!!!")
    # execucao da api em modo debug
    app.run(debug=True)
