from flask_restful import Resource, reqparse
from resources.teste import dados


class DadosReceive(Resource):
    # implementacao de metodo get para teste
    def get(self):
        
        # resultado da implementacao get
        return {'Dados': dados}

class DadoReceive(Resource):

    def get(self, dado_id):
        
        for dado in dados:
                
            if dado['dado_id'] == dado_id:
                return dado

        return {'message': 'Dado not found'}, 404

    def post(self, dado_id):

        argumentos = reqparse.RequestParser()

        argumentos.add_argument('ano')
        argumentos.add_argument('mes')
        argumentos.add_argument('dia')
        argumentos.add_argument('hora')
        argumentos.add_argument('minuto')
        argumentos.add_argument('segundo')
        argumentos.add_argument('milissegundos')
        argumentos.add_argument('corrente')
        argumentos.add_argument('tensao')
        argumentos.add_argument('temperatura')
        argumentos.add_argument('type')

        dados = argumentos.parse_args()

        novo_dado = {
            'dado_id' : dado_id,
            'ano' : dados['ano'],
            'mes' : dados['mes'],
            'dia' : dados['dia'],
            'hora' : dados['hora'],
            'minuto' : dados['minuto'],
            'segundo' : dados['segundo'],
            'milissegundos' : dados['milissegundos'],
            'corrente' : dados['corrente'],
            'tensao' : dados['temsao'],
            'temperatura' : dados['temperatura'],
            'type': dados['type']
        }

        dados.append(novo_dado)

        return novo_dado, 200
    
    def put(self):
        ...
    
    def delete(self):
        ...