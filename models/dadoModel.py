

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
        dia = str(self.dia) + "/" + str(self.mes) + "/" + str(self.ano)
        hora = str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo)
        tensao =str(self.tensao)
        corrente = str(self.corrente)  
        temperatura = str(self.temperatura)
        return [[dia, hora, tensao, corrente, temperatura],]
    