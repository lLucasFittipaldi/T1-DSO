from abc import ABC
from datetime import date, time

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf)
        self.data_nascimento = data_nascimento

    def is_maior_de_idade(self, data_referencia: date) -> bool:
       # Testa se o paciente tem 18 anos completos na data informada.
        idade = data_referencia.year - self.data_nascimento.year - \
                ((data_referencia.month, data_referencia.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade >= 18

class Profissional(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self.especialidade = especialidade
        self.registro_profissional = registro_profissional
