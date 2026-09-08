from abc import ABC, abstractmethod

class Carteira:
    def __init__(self, valor):
        self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    def __eq__(self, other):
        if self.__saldo == other.saldo:
            return True
        return False
