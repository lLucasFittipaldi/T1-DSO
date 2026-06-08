from datetime import date, time
from model.atendimento import Atendimento, Procedimento
from model.pagamento import PagamentoDinheiro, PagamentoPix, PagamentoCartao

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        # Cria uma lista vazia para armazenar os atendimentos e um contador para o próximo ID
        self.__atendimentos = []
        self.__proximo_id = 1

    def cadastrar(self, data_str: str, horario_inicio_str: str, horario_fim_str: str, valor: float,
                  nome_clinica: str, cidade_clinica: str,
                  cpf_paciente: str, cpf_profissional: str, nome_tipo: str):
        
        try:
            ano, mes, dia = map(int, data_str.split('-'))
            data_atendimento = date(ano, mes, dia)
            
            h_ini, m_ini = map(int, horario_inicio_str.split(':'))
            hora_inicio = time(h_ini, m_ini)
            
            h_fim, m_fim = map(int, horario_fim_str.split(':'))
            hora_fim = time(h_fim, m_fim)
        except Exception:
            raise ValueError("Formato de data ou hora inválido. Use AAAA-MM-DD e HH:MM.")

        clinica = None
        for c in self.__controlador_sistema.controlador_clinica.listar():
            if c.nome.lower() == nome_clinica.lower() and c.cidade.lower() == cidade_clinica.lower():
                clinica = c
                break
        if not clinica:
            raise ValueError("Clínica não encontrada com o nome e cidade fornecidos.")

        paciente = None
        for p in self.__controlador_sistema.controlador_paciente.listar():
            if p.cpf == cpf_paciente:
                paciente = p
                break
        if not paciente:
            raise ValueError("Paciente não encontrado com o CPF fornecido.")

        profissional = None
        for prof in self.__controlador_sistema.controlador_profissional.listar():
            if prof.cpf == cpf_profissional:
                profissional = prof
                break
        if not profissional:
            raise ValueError("Profissional não encontrado com o CPF fornecido.")

        tipo = self.__controlador_sistema.controlador_tipo_atendimento.buscar(nome_tipo)

        atendimento = Atendimento(clinica, paciente, profissional, data_atendimento, 
                                  hora_inicio, hora_fim, tipo, valor)
        # Atribui o ID atual ao novo atendimento e logo em seguida soma +1 para o próximo atendimento
        atendimento.id = self.__proximo_id
        self.__proximo_id += 1
        self.__atendimentos.append(atendimento)

    def remover(self, index: int):
        if index < 0 or index >= len(self.__atendimentos):
            raise ValueError("Atendimento não encontrado.")
        self.__atendimentos.pop(index)

    def alterar(self, index: int, data_str=None, horario_inicio_str=None, horario_fim_str=None, novo_valor_base=None):
        if index < 0 or index >= len(self.__atendimentos):
            raise ValueError("Atendimento não encontrado.")
        
        atendimento = self.__atendimentos[index]
        
        if data_str:
            try:
                ano, mes, dia = map(int, data_str.split('-'))
                atendimento.data_atendimento = date(ano, mes, dia)
            except Exception:
                raise ValueError("Formato de data inválido. Use AAAA-MM-DD.")
                
        if horario_inicio_str:
            try:
                h, m = map(int, horario_inicio_str.split(':'))
                atendimento.hora_inicio = time(h, m)
            except Exception:
                raise ValueError("Formato de horário de início inválido. Use HH:MM.")
                
        if horario_fim_str:
            try:
                h, m = map(int, horario_fim_str.split(':'))
                atendimento.hora_fim = time(h, m)
            except Exception:
                raise ValueError("Formato de horário de fim inválido. Use HH:MM.")
                
        if novo_valor_base is not None:
            atendimento.valor_base = novo_valor_base
            
        atendimento._validar_regras()

    def buscar(self, id_atendimento: int) -> Atendimento:
        # percorre a lista de atendimentos um por um
        for a in self.__atendimentos:
            if a.id == id_atendimento:
                return a # retorna  o objeto assim que encontra, parando a busca
            # se chegar ao final da lista sem encontrar, lança um erro
        raise ValueError("Atendimento não encontrado.")

    def listar(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento cadastrado.")
        return list(self.__atendimentos)

    def adicionar_procedimento(self, id_atendimento: int, procedimento: Procedimento):
        atendimento = self.buscar(id_atendimento)
        atendimento.adicionar_procedimento(procedimento)

    def remover_procedimento(self, id_atendimento: int, indice: int):
        atendimento = self.buscar(id_atendimento)
        if indice < 0 or indice >= len(atendimento.procedimentos):
            raise ValueError("Procedimento não encontrado.")
        atendimento.procedimentos.pop(indice)

    def registrar_pagamento_dinheiro(self, id_atendimento: int, data_pagamento, valor_pago: float):
        atendimento = self.buscar(id_atendimento)
        pagamento = PagamentoDinheiro(data_pagamento, atendimento.paciente, valor_pago)
        atendimento.registrar_pagamento(pagamento)

    def registrar_pagamento_pix(self, id_atendimento: int, data_pagamento,
                                valor_pago: float, cpf_pagador: str):
        atendimento = self.buscar(id_atendimento)
        pagamento = PagamentoPix(data_pagamento, atendimento.paciente, valor_pago, cpf_pagador)
        atendimento.registrar_pagamento(pagamento)

    def registrar_pagamento_cartao(self, id_atendimento: int, data_pagamento,
                                   valor_pago: float, numero_cartao: str, bandeira: str):
        atendimento = self.buscar(id_atendimento)
        pagamento = PagamentoCartao(data_pagamento, atendimento.paciente,
                                    valor_pago, numero_cartao, bandeira)
        atendimento.registrar_pagamento(pagamento)

      # Relatórios ->  esqueci de colocar no menu de atendimento.

    def relatorio_clinicas_mais_atendimentos(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento registrado.")
        contagem = []
        for a in self.__atendimentos:
            encontrou = False
            for item in contagem:
                if item[0] == a.clinica.nome:
                    item[1] += 1
                    encontrou = True
                    break
            if not encontrou:
                contagem.append([a.clinica.nome, 1])
        contagem.sort(key=lambda x: x[1], reverse=True)
        return contagem

    def relatorio_atendimentos_caros_baratos(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento registrado.")
        ordenados = sorted(self.__atendimentos, key=lambda a: a.calcular_valor_total(), reverse=True)
        return ordenados

    def relatorio_procedimentos_populares(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento registrado.")
        contagem = []
        for a in self.__atendimentos:
            for proc in a.procedimentos:
                encontrou = False
                for item in contagem:
                    if item[0] == proc.descricao:
                        item[1] += 1
                        encontrou = True
                        break
                if not encontrou:
                    contagem.append([proc.descricao, 1])
        if not contagem:
            raise ValueError("Nenhum procedimento registrado.")
        contagem.sort(key=lambda x: x[1], reverse=True)
        return contagem

    def relatorio_procedimentos_caros_baratos(self):
        todos = []
        for a in self.__atendimentos:
            for proc in a.procedimentos:
                todos.append(proc)
        if not todos:
            raise ValueError("Nenhum procedimento registrado.")
        todos.sort(key=lambda p: p.custo, reverse=True)
        return todos