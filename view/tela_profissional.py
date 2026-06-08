from model.pessoa import Profissional

class TelaProfissional:
    def __init__(self, controlador_profissional):
        self.__controlador_profissional = controlador_profissional

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PROFISSIONAL ===")
            print("1. Cadastrar profissional")
            print("2. Remover profissional")
            print("3. Alterar profissional")
            print("4. Listar profissionais")
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
            nome = input("Nome: ").strip()
            celular = input("Celular: ").strip()
            cpf = input("CPF (somente números): ").strip()
            especialidade = input("Especialidade: ").strip()
            registro = input("Registro profissional: ").strip()
            profissional = Profissional(nome, celular, cpf, especialidade, registro)
            self.__controlador_profissional.cadastrar(profissional)
            print("Profissional cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            cpf = input("CPF do profissional a remover: ").strip()
            self.__controlador_profissional.remover(cpf)
            print("Profissional removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            # ao deixar a entrada em branco, envia None para o controlador, sinalizando que o valor deve ser mantido
            cpf = input("CPF do profissional a alterar: ").strip()
            print("Deixe em branco para manter o valor atual.")
            novo_nome = input("Novo nome: ").strip() or None
            novo_celular = input("Novo celular: ").strip() or None
            nova_especialidade = input("Nova especialidade: ").strip() or None
            novo_registro = input("Novo registro profissional: ").strip() or None
            self.__controlador_profissional.alterar(cpf, novo_nome, novo_celular,
                                                    nova_especialidade, novo_registro)
            print("Profissional alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            profissionais = self.__controlador_profissional.listar()
            print("\n=== PROFISSIONAIS ===")
            for i, p in enumerate(profissionais):
                print(f"{i+1}. {p.nome} | CPF: {p.cpf} | "
                      f"Celular: {p.celular} | "
                      f"Especialidade: {p.especialidade} | "
                      f"Registro: {p.registro_profissional}")
        except ValueError as e:
            print(f"Erro: {e}")
