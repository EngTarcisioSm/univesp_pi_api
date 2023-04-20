# import de bibliotecas necessárias 
from flask import Flask
from flask_restful import Api

from resources.dados import DadosReceive, DadoReceive
from resources.findID import FindID

# criação dos objetos 
app = Flask(__name__)
api = Api(app)

# adicionando recurso na api
api.add_resource(DadosReceive, '/dados')
api.add_resource(DadoReceive, '/dado/<int:dado_id>')
api.add_resource(FindID, '/lastID')



if __name__ == "__main__":

    print("Begin!!!")
    # execucao da api em modo debug
    app.run(debug=True)
