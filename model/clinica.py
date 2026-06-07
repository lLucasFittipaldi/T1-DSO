
from datetime import time

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str, hora_abertura: time, hora_fechamento: time):
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.hora_abertura = hora_abertura
        self.hora_fechamento = hora_fechamento

    def atende_no_horario(self, hora_inicio: time, hora_fim: time) -> bool:
        """Verifica se o horário passado está dentro do expediente da clínica."""
        return self.hora_abertura <= hora_inicio and hora_fim <= self.hora_fechamento
