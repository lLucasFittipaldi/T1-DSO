from model.pessoa import Profissional


class ControladorProfissional:
    def __init__(self):
        self.__profissionais = []

    def cadastrar(self, profissional: Profissional):
        for p in self.__profissionais:
            if p.cpf == profissional.cpf:
                raise ValueError("Já existe um profissional com esse CPF.")
            if p.registro_profissional == profissional.registro_profissional:
                raise ValueError("Já existe um profissional com esse registro profissional.")
        self.__profissionais.append(profissional)

    def remover(self, cpf: str):
        for p in self.__profissionais:
            if p.cpf == cpf:
                self.__profissionais.remove(p)
                return
        raise ValueError("Profissional não encontrado.")

    def alterar(self, cpf: str, novo_nome=None, novo_celular=None,
                nova_especialidade=None, novo_registro=None):
        profissional = self.buscar(cpf)
        if novo_nome:
            profissional.nome = novo_nome
        if novo_celular:
            profissional.celular = novo_celular
        if nova_especialidade:
            profissional.especialidade = nova_especialidade
        if novo_registro:
            profissional.registro_profissional = novo_registro

    def buscar(self, cpf: str) -> Profissional:
        for p in self.__profissionais:
            if p.cpf == cpf:
                return p
        raise ValueError("Profissional não encontrado.")

    def listar(self):
        if not self.__profissionais:
            raise ValueError("Nenhum profissional cadastrado.")
        return list(self.__profissionais)