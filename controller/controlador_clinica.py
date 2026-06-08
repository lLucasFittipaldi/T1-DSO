from model.clinica import Clinica


class ControladorClinica:
    def __init__(self):
        self.__clinicas = []

    def cadastrar(self, clinica: Clinica):
        for c in self.__clinicas:
            if c.nome == clinica.nome and c.cidade == clinica.cidade:
                raise ValueError("Já existe uma clínica com esse nome nessa cidade.")
        self.__clinicas.append(clinica)

    def remover(self, nome: str, cidade: str):
        for c in self.__clinicas:
            if c.nome == nome and c.cidade == cidade:
                self.__clinicas.remove(c)
                return
        raise ValueError("Clínica não encontrada.")

    def alterar(self, nome: str, cidade: str, novo_nome=None, nova_cidade=None,
                nova_descricao=None, nova_abertura=None, novo_fechamento=None):
        clinica = self.buscar(nome, cidade)
        if novo_nome:
            clinica.nome = novo_nome
        if nova_cidade:
            clinica.cidade = nova_cidade
        if nova_descricao:
            clinica.descricao = nova_descricao
        if nova_abertura:
            clinica.hora_abertura = nova_abertura
        if novo_fechamento:
            clinica.hora_fechamento = novo_fechamento

    def buscar(self, nome: str, cidade: str) -> Clinica:
        for c in self.__clinicas:
            if c.nome == nome and c.cidade == cidade:
                return c
        raise ValueError("Clínica não encontrada.")

    def listar(self):
        if not self.__clinicas:
            raise ValueError("Nenhuma clínica cadastrada.")
        return list(self.__clinicas)