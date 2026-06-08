from datetime import time
from model.clinica import Clinica


class TelaClinica:
    def __init__(self, controlador_clinica):
        self.__controlador_clinica = controlador_clinica

    def mostrar_menu(self):
        while True:
            print("\n=== MENU CLÍNICA ===")
            print("1. Cadastrar clínica")
            print("2. Remover clínica")
            print("3. Alterar clínica")
            print("4. Listar clínicas")
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

    def _ler_horario(self, mensagem: str) -> time:
        hora_str = input(mensagem).strip()
        partes = hora_str.split(":")
        return time(int(partes[0]), int(partes[1]))

    def cadastrar(self):
        try:
            nome = input("Nome da clínica: ").strip()
            cidade = input("Cidade: ").strip()
            descricao = input("Descrição: ").strip()
            abertura = self._ler_horario("Hora de abertura (HH:MM): ")
            fechamento = self._ler_horario("Hora de fechamento (HH:MM): ")
            clinica = Clinica(nome, cidade, descricao, abertura, fechamento)
            self.__controlador_clinica.cadastrar(clinica)
            print("Clínica cadastrada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            nome = input("Nome da clínica a remover: ").strip()
            cidade = input("Cidade da clínica: ").strip()
            self.__controlador_clinica.remover(nome, cidade)
            print("Clínica removida com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            nome = input("Nome da clínica a alterar: ").strip()
            cidade = input("Cidade da clínica: ").strip()
            print("Deixe em branco para manter o valor atual.")
            novo_nome = input("Novo nome: ").strip() or None
            nova_cidade = input("Nova cidade: ").strip() or None
            nova_descricao = input("Nova descrição: ").strip() or None
            abertura_str = input("Nova hora de abertura (HH:MM): ").strip()
            fechamento_str = input("Nova hora de fechamento (HH:MM): ").strip()
            nova_abertura = None
            novo_fechamento = None
            if abertura_str:
                partes = abertura_str.split(":")
                nova_abertura = time(int(partes[0]), int(partes[1]))
            if fechamento_str:
                partes = fechamento_str.split(":")
                novo_fechamento = time(int(partes[0]), int(partes[1]))
            self.__controlador_clinica.alterar(nome, cidade, novo_nome, nova_cidade,
                                               nova_descricao, nova_abertura, novo_fechamento)
            print("Clínica alterada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            clinicas = self.__controlador_clinica.listar()
            print("\n=== CLÍNICAS ===")
            for i, c in enumerate(clinicas):
                print(f"{i+1}. {c.nome} | Cidade: {c.cidade} | "
                      f"Funcionamento: {c.hora_abertura.strftime('%H:%M')} - "
                      f"{c.hora_fechamento.strftime('%H:%M')} | Descrição: {c.descricao}")
        except ValueError as e:
            print(f"Erro: {e}")
