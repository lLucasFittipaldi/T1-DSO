from datetime import date, time
from typing import List
from model.clinica import Clinica
from model.pessoa import Paciente, Profissional
from model.pagamento import Pagamento

class TipoAtendimento:
    def __init__(self, descricao: str):
        self.descricao = descricao

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional_responsavel: Profissional):
        self.descricao = descricao
        self.custo = custo
        self.profissional_responsavel = profissional_responsavel

class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, 
                 data_atendimento: date, hora_inicio: time, hora_fim: time, 
                 tipo: TipoAtendimento, valor_base: float):
        self.id = None
        self.clinica = clinica
        self.paciente = paciente
        self.profissional = profissional
        self.data_atendimento = data_atendimento
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.tipo = tipo
        self.valor_base = valor_base
        
        self.procedimentos: List[Procedimento] = []
        self.pagamentos: List[Pagamento] = []

        # Valida as regras
        self._validar_regras()

    def _validar_regras(self):
        # Somente pacientes com mais de 18 anos completos.
        if not self.paciente.is_maior_de_idade(self.data_atendimento):
            raise ValueError("O paciente deve ter mais de 18 anos para realizar o atendimento de forma independente.")
        
        # Ocorrer dentro do período de funcionamento.
        if not self.clinica.atende_no_horario(self.hora_inicio, self.hora_fim):
            raise ValueError("O horário do atendimento está fora do período de funcionamento da clínica.")

    def adicionar_procedimento(self, procedimento: Procedimento):
        self.procedimentos.append(procedimento)

    def registrar_pagamento(self, pagamento: Pagamento):
        # Os pagamentos devem ser realizados até a data do atendimento.
        if pagamento.data_pagamento > self.data_atendimento:
            raise ValueError("A data de pagamento não pode ser posterior à data do atendimento.")
        
        self.pagamentos.append(pagamento)

    def calcular_valor_total(self) -> float:
       # Retorna a soma do valor base da consulta com os custos dos procedimentos
        valor_procedimentos = sum(p.custo for p in self.procedimentos)
        return self.valor_base + valor_procedimentos

    def calcular_valor_restante(self) -> float:
       # Subtrai o total já pago do valor total do atendimento
        total_pago = sum(p.valor_pago for p in self.pagamentos)
        return self.calcular_valor_total() - total_pago