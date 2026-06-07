from datetime import date
from model.pessoa import Paciente
from model.pagamento import PagamentoDinheiro

# 1. Criando um paciente de teste
data_nasc = date(2000, 1, 15)
paciente_teste = Paciente(nome="Lucas", celular="9999-9999", cpf="123", data_nascimento=data_nasc)

# 2. Criando um pagamento para esse paciente
data_hoje = date(2026, 6, 7)
pagamento_teste = PagamentoDinheiro(data_pagamento=data_hoje, paciente=paciente_teste, valor_pago=150.0)

print("SUCESSO! O Python encontrou os arquivos.")
print(f"O pagamento de R$ {pagamento_teste.valor_pago} do paciente {pagamento_teste.paciente.nome} foi registrado.")