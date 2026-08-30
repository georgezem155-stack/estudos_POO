"""
Template Method Pattern - Bebidas Quentes
-------------------------------------------
Este projeto demonstra o padrão de projeto Template Method:
a classe abstrata (BebidaQuente) define o algoritmo geral de preparo,
enquanto as subclasses (Cafe, Cha) implementam os passos específicos
de cada bebida (misturar e servir).

O passo de ferver água é comum a todas as bebidas e fica pronto
na classe mãe - nenhuma subclasse precisa reescrevê-lo.
"""

from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    """Classe abstrata que define o algoritmo geral de preparo."""

    def preparar_bebida(self):
        """Método template: define a ordem fixa dos passos de preparo."""
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        """Passo comum a todas as bebidas quentes."""
        print("1. Fervendo água a 100 graus celsius...")

    @abstractmethod
    def misturar(self):
        """Cada bebida define seu próprio jeito de misturar."""
        pass

    @abstractmethod
    def servir(self):
        """Cada bebida define seu próprio jeito de servir."""
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Misturando o pó de café com água quente...")

    def servir(self):
        print("3. Servindo na caneca grande com café.")
        print("--- Bebida pronta ---")


class Cha(BebidaQuente):
    def misturar(self):
        print("2. Misturando o chá na água quente...")

    def servir(self):
        print("3. Servindo o chá em uma caneca grande.")
        print("--- Bebida pronta ---")


if __name__ == "__main__":
    print("== Preparando café ==")
    cafe = Cafe()
    cafe.preparar_bebida()

    print()

    print("== Preparando chá ==")
    cha = Cha()
    cha.preparar_bebida()
