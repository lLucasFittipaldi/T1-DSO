from model.atendimento import TipoAtendimento


class TelaTipoAtendimento:
    def __init__(self, controlador_tipo_atendimento):
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento

    def mostrar_menu(self):
        while True:
            print("\n=== MENU TIPO DE ATENDIMENTO ===")
            print("1. Cadastrar tipo")
            print("2. Remover tipo")
            print("3. Alterar tipo")
            print("4. Listar tipos")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.remover()
            elif opcao == "3":
                self.alterar()
            elif opcao == "4":
                self.listar()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def cadastrar(self):
        try:
            descricao = input("Descrição do tipo (ex: Consulta, Exame, Retorno): ").strip()
            tipo = TipoAtendimento(descricao)
            self.__controlador_tipo_atendimento.cadastrar(tipo)
            print("Tipo de atendimento cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            descricao = input("Descrição do tipo a remover: ").strip()
            self.__controlador_tipo_atendimento.remover(descricao)
            print("Tipo removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            descricao = input("Descrição atual do tipo: ").strip()
            nova_descricao = input("Nova descrição: ").strip()
            self.__controlador_tipo_atendimento.alterar(descricao, nova_descricao)
            print("Tipo alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            tipos = self.__controlador_tipo_atendimento.listar()
            print("\n=== TIPOS DE ATENDIMENTO ===")
            for i, t in enumerate(tipos):
                print(f"{i+1}. {t.descricao}")
        except ValueError as e:
            print(f"Erro: {e}")