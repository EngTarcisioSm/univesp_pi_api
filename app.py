# import de bibliotecas necessárias 
from flask import Flask
from flask_restful import Resource, Api


dados = [
    {
        'dados_id': 1,
        'corrente': 1.0343,
        'tensao': 110,
        'temperatura': 29
    },
    {
        'dados_id': 2,
        'corrente': 10,
        'tensao': 220,
        'temperatura': 29
    },
    {
        'dados_id': 3,
        'corrente': 0.04,
        'tensao': 50,
        'temperatura': 15
    }
]

# criação dos objetos 
app = Flask(__name__)
api = Api(app)


class DadosReceiveDB(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': dados}

class DadosReceiveSheets(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': dados}   

# adicionando recurso na api
api.add_resource(DadosReceiveDB, '/dados_db')
api.add_resource(DadosReceiveSheets, '/dados_sheet')


if __name__ == "__main__":

    print("Begin!!!")
    # execucao da api em modo debug
    app.run(debug=True)
