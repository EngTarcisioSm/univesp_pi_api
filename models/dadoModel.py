

class DadoModel:

    def __init__(self, dado_id, ano, mes, dia, hora, minuto, segundo, milissegundos, corrente, tensao, temperatura, type) -> None:
        
        self.dado_id = dado_id
        self.ano = int(ano)
        self.mes = int(mes)
        self.dia = int(dia)
        self.hora = int(hora)
        self.minuto = int(minuto)
        self.segundo = int(segundo)
        self.milissegundos = int(milissegundos)
        self.corrente = float(corrente)
        self.tensao = float(tensao)
        self.temperatura = float(temperatura)
        self.type = type

    def json(self):
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