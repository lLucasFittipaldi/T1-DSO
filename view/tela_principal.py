from view.tela_clinica import TelaClinica
from view.tela_paciente import TelaPaciente
from view.tela_profissional import TelaProfissional
from view.tela_tipo_atendimento import TelaTipoAtendimento
from view.tela_atendimento import TelaAtendimento


class TelaPrincipal:
    def __init__(self, controlador_sistema):
        cs = controlador_sistema
        self.__tela_clinica = TelaClinica(cs.controlador_clinica)
        self.__tela_paciente = TelaPaciente(cs.controlador_paciente)
        self.__tela_profissional = TelaProfissional(cs.controlador_profissional)
        self.__tela_tipo_atendimento = TelaTipoAtendimento(cs.controlador_tipo_atendimento)
        self.__tela_atendimento = TelaAtendimento(cs.controlador_atendimento)

    def mostrar_menu(self):
        while True:
            print("\n=============================")
            print("  SISTEMA DE CLÍNICAS")
            print("=============================")
            print("1. Clínicas")
            print("2. Pacientes")
            print("3. Profissionais")
            print("4. Tipos de atendimento")
            print("5. Atendimentos")
            print("0. Sair")
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.__tela_clinica.mostrar_menu()
            elif opcao == "2":
                self.__tela_paciente.mostrar_menu()
            elif opcao == "3":
                self.__tela_profissional.mostrar_menu()
            elif opcao == "4":
                self.__tela_tipo_atendimento.mostrar_menu()
            elif opcao == "5":
                self.__tela_atendimento.mostrar_menu()
            elif opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção inválida.")