from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('Ligado!')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligado!')

    @property
    def marca(self):
        return 'LG'


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado...')
        print('Ligado!')

    def desligar(self):
        print('Desligando o Ar Condicionado...')
        print('Desligado!')

    @property
    def marca(self):
        return 'LG'


controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
