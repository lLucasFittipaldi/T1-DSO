from abc import ABC
from datetime import date
from model.pessoa import Paciente

class Pagamento(ABC):
    def __init__(self, data_pagamento: date, paciente: Paciente, valor_pago: float):
        self.data_pagamento = data_pagamento
        self.paciente = paciente
        self.valor_pago = valor_pago

class PagamentoDinheiro(Pagamento):
    def __init__(self, data_pagamento: date, paciente: Paciente, valor_pago: float):
        super().__init__(data_pagamento, paciente, valor_pago)

class PagamentoPix(Pagamento):
    def __init__(self, data_pagamento: date, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data_pagamento, paciente, valor_pago)
        self.cpf_pagador = cpf_pagador

class PagamentoCartao(Pagamento):
    def __init__(self, data_pagamento: date, paciente: Paciente, valor_pago: float, numero_cartao: str, bandeira: str):
        super().__init__(data_pagamento, paciente, valor_pago)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira