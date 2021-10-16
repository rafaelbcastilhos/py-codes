from abc import ABC
from animal import Animal


class Ave(Animal, ABC):
    def __init__(self, tamanhoPasso, altura_voo):
        super().__init__(tamanhoPasso)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo

    def mover(self):
        return f"ANIMAL: DESLOCOU {self.tamanho_passo} VOANDO"
