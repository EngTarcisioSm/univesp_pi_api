

class DadoModel:

    def __init__(self, dado_id, ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type) -> None:
        
        self.dado_id = dado_id
        self.ano = str(ano)
        self.mes = str(mes)
        self.dia = str(dia)
        self.hora = str(hora)
        self.minuto = str(minuto)
        self.segundo = str(segundo)
        self.milissegundos = str(milissegundos)
        self.corrente = str(corrente)
        self.tensao = str(tensao)
        self.temperatura = str(temperatura)
        self.type = type

    def json(self)->dict:
        return {
            'dado_id': self.dado_id,
            'ano': self.ano,
            'mes': self.mes,
            'dia': self.dia,
            'hora': self.hora,
            'minuto': self.minuto,
            'segundo': self.segundo,
            'milissegundos': self.milissegundos,
            'corrente': self.corrente,
            'tensao': self.tensao,
            'temperatura': self.temperatura,
            'type': self.type
        }
    
    def dataSendSheets(self):
        tempo = str(self.dia) + "/" + str(self.mes) + "/" + str(self.ano) + "-" + str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo) + ":" + str(self.milissegundos)
        data = "U:" + str(self.tensao) + "|" + "I:" + str(self.corrente) + "|" + "T:" + str(self.temperatura)  
        return [[tempo, data],]