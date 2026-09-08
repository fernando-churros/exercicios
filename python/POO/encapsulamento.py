from abc import ABC, abstractmethod
import hashlib
from getpass import getpass

#28 Implemente um termostato com POO: min 16 | max 30 | on 24 | inc 0,5
class Termostato:
    t_min = 16
    t_max = 30

    def __init__(self):
        self.__temperatura = 24
    
    @property
    def temperatura(self):
         return self.__temperatura

    @temperatura.setter
    def temperatura(self, t):
        if t % 0.5 != 0:
            raise ValueError(f'Temperatura {t}ºC é inválida')

        if t < t_min:
            self.__temperatura = t_min
        elif t > t_max:
            self.__temperatura = t_max
        else:
            self.__temperatura = t
    
    @property
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'


#29 Simule um diário secreto com POO
class Diario:
    def __init__(self, senha = '0000'):
        self.__segredos = []
        self.__senha = hashlib.sha256(senha.encode()).hexdigest()

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha):
        if self.__senha == hashlib.sha256(senha.encode()).hexdigest():
            return self.__leitura()

        return 'Senha Inválida'
    
    def __leitura(self):
        pag = ['Segredos Secretos']
        for i, x in enumerate(self.__segredos):
            pag.append(f'{i + 1}º - {x}')

        return '\n'.join(pag)

    @property
    def senha(self):
        raise PermissionError('Permissão Negada')

    @senha.setter
    def senha(self, senha):
        if self.__senha == hashlib.sha256(senha[0].encode()).hexdigest():
            self.__senha = hashlib.sha256(senha[1].encode()).hexdigest()
            print('senha alterada')
        else:
            print('senha inválida')


#30 Crie uma classe que gerencie a hash SHA256 de uma senha
class Credencial:
    def __init__(self):
        self.__hash_senha = None

    def validar(self, senha):
        verify_senha = hashlib.sha256(senha.encode()).hexdigest()
        if self.__hash_senha == verify_senha:
            return 'Senha correta'
        return 'Senha incorreta'

    @property
    def senha(self):
        return self.__hash_senha

    @senha.setter
    def senha(self, senha):
        if len(senha) > 0:
            self.__hash_senha = hashlib.sha256(senha.encode()).hexdigest()
        else:
            raise ValueError('Senha vazia.')


#31 Crie a classe que representa um retângulo pelas suas medidas e area
class Retangulo:
    def __init__(self, base = None, altura = None):
        self.base = base
        self._altura:float = altura
        self._area = None

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, b):
        if isinstance(b, (int, float)):
            self._base:float = b

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, a):
        if isinstance(a, (int, float)): 
            self._altura = a
    
    @property
    def area(self):
        if self._base is not None and self._altura is not None:
            self._area = self._base * self._altura
            return self._area
        else:
            return f'base[{self._base}] ou altura[{self._altura}], não podem ser None'
    
    @property
    def medidas(self):
        return (self._base, self._altura)

    @medidas.setter
    def medidas(self, m):
        self._base = m[0]
        self._altura = m[1]


#32 Aprimore o exercicio da conta bancaria, aplicando encapsulamento
class ContaBancaria:
    def __init__(self, ID, titular, chave = None):
        self._id = ID
        self._titular = titular
        self.__saldo = 0
        self.__hash = chave
        if self.__hash is None:
            self._pede_senha()
    
    def _pede_senha(self):
        c = getpass('Senha:', echo_char='*')
        self.__hash = hashlib.sha256(c.encode('utf-8')).hexdigest()

    def _validar_senha(self, chave):
        if self.__hash == hashlib.sha256(chave.encode('utf-8')).hexdigest():
            return True
        return False

    def depositar(self, valor):
        self.__saldo += abs(valor)
        print(f'Deposito de {valor}, concluido')

    def sacar(self, valor, chave = None):
        if chave is None:
            chave = getpass('Senha', echo_char='*')

        if self._validar_senha(chave):
            self.__saldo -= abs(valor)
        else:
            print('Senha inválida')
    
    @property
    def nome(self):
        return self._titular
    @nome.setter
    def nome(self, nome):
        if self._validar_senha(getpass('Senha: ', echo_char='*')):
            self._titular = nome


#33 Implemente a seguinte estrutura de diagrama de classe
class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self, n):
        if 1900 < n < 2025:
            self._nascimento = n
        else:
            raise ValueError('Ano inválido')
    
    @property
    def idade(self):
        return 2026 - self._nascimento


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['Inglês', 'Programação']
        self.curso = curso

    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self, c):
        if c.title() in self.cursos_oficiais:
            self._curso = c.title()
        else:
            raise ValueError('Curso inválido')

    def add_curso(self, c):
        self.cursos_oficiais.append(c.title())


