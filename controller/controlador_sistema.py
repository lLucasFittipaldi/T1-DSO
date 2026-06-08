from controller.controlador_clinica import ControladorClinica
from controller.controlador_paciente import ControladorPaciente
from controller.controlador_profissional import ControladorProfissional
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from controller.controlador_atendimento import ControladorAtendimento
from view.tela_principal import TelaPrincipal

class ControladorSistema:
    def __init__(self):
        self.__controlador_clinica = ControladorClinica()
        self.__controlador_paciente = ControladorPaciente()
        self.__controlador_profissional = ControladorProfissional()
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento()
        
        self.__controlador_atendimento = ControladorAtendimento(self)
        
        self.__tela_principal = TelaPrincipal(self)

    def iniciar(self):
        self.__tela_principal.mostrar_menu()

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_profissional(self):
        return self.__controlador_profissional

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento