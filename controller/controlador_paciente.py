from model.pessoa import Paciente


class ControladorPaciente:
    def __init__(self):
        self.__pacientes = []

    def cadastrar(self, paciente: Paciente):
        for p in self.__pacientes:
            if p.cpf == paciente.cpf:
                raise ValueError("Já existe um paciente com esse CPF.")
        self.__pacientes.append(paciente)

    def remover(self, cpf: str):
        for p in self.__pacientes:
            if p.cpf == cpf:
                self.__pacientes.remove(p)
                return
        raise ValueError("Paciente não encontrado.")

    def alterar(self, cpf: str, novo_nome=None, novo_celular=None):
        paciente = self.buscar(cpf)
        if novo_nome:
            paciente.nome = novo_nome
        if novo_celular:
            paciente.celular = novo_celular

    def buscar(self, cpf: str) -> Paciente:
        for p in self.__pacientes:
            if p.cpf == cpf:
                return p
        raise ValueError("Paciente não encontrado.")

    def listar(self):
        if not self.__pacientes:
            raise ValueError("Nenhum paciente cadastrado.")
        return list(self.__pacientes)