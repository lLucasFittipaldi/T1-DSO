from datetime import date
from model.pessoa import Paciente


class TelaPaciente:
    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PACIENTE ===")
            print("1. Cadastrar paciente")
            print("2. Remover paciente")
            print("3. Alterar paciente")
            print("4. Listar pacientes")
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

    def _ler_data(self, mensagem: str) -> date:
        data_str = input(mensagem).strip()
        partes = data_str.split("/")
        return date(int(partes[2]), int(partes[1]), int(partes[0]))

    def cadastrar(self):
        try:
            nome = input("Nome: ").strip()
            celular = input("Celular: ").strip()
            cpf = input("CPF (somente números): ").strip()
            data_nascimento = self._ler_data("Data de nascimento (DD/MM/AAAA): ")
            paciente = Paciente(nome, celular, cpf, data_nascimento)
            self.__controlador_paciente.cadastrar(paciente)
            print("Paciente cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            cpf = input("CPF do paciente a remover: ").strip()
            self.__controlador_paciente.remover(cpf)
            print("Paciente removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            cpf = input("CPF do paciente a alterar: ").strip()
            print("Deixe em branco para manter o valor atual.")
            novo_nome = input("Novo nome: ").strip() or None
            novo_celular = input("Novo celular: ").strip() or None
            self.__controlador_paciente.alterar(cpf, novo_nome, novo_celular)
            print("Paciente alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            pacientes = self.__controlador_paciente.listar()
            print("\n=== PACIENTES ===")
            for i, p in enumerate(pacientes):
                print(f"{i+1}. {p.nome} | CPF: {p.cpf} | "
                      f"Celular: {p.celular} | "
                      f"Nascimento: {p.data_nascimento.strftime('%d/%m/%Y')}")
        except ValueError as e:
            print(f"Erro: {e}")