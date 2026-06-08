from model.atendimento import TipoAtendimento


class ControladorTipoAtendimento:
    def __init__(self):
        self.__tipos = []

    def cadastrar(self, tipo: TipoAtendimento):
        for t in self.__tipos:
            if t.descricao.lower() == tipo.descricao.lower():
                raise ValueError("Já existe um tipo de atendimento com essa descrição.")
        self.__tipos.append(tipo)

    def remover(self, descricao: str):
        for t in self.__tipos:
            if t.descricao.lower() == descricao.lower():
                self.__tipos.remove(t)
                return
        raise ValueError("Tipo de atendimento não encontrado.")

    def alterar(self, descricao: str, nova_descricao: str):
        tipo = self.buscar(descricao)
        tipo.descricao = nova_descricao

    def buscar(self, descricao: str) -> TipoAtendimento:
        for t in self.__tipos:
            if t.descricao.lower() == descricao.lower():
                return t
        raise ValueError("Tipo de atendimento não encontrado.")

    def listar(self):
        if not self.__tipos:
            raise ValueError("Nenhum tipo de atendimento cadastrado.")
        return list(self.__tipos)