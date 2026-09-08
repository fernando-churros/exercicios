from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

#34 Crie a seguinte estrutura de classes para calcular bônus salarial
class Funcionario(ABC):
    def __init__(self, nome:str = 'Unknown', salario:int|float = 1650):
        self.nome = nome
        self.__salario = None
        self.salario = salario

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, value: int | float):
        if value < 1650:
            raise ValueError('Necessita de uma salário minimo de R$1,650.00.')

        if self.salario is not None and value < self.salario:
            raise ValueError('Não é possivel reduzir o salário de um funcionário.')

        self.__salario = value
    
    @abstractmethod
    def bonus(self):
        pass

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__}, o bonus será de R${self.bonus:,.2f}'
        

class Design(Funcionario):
    BONUS = 0.08
    
    @property
    def bonus(self):
        return self.salario * self.BONUS


class Desenvolvedor(Funcionario):
    BONUS = 0.1

    @property
    def bonus(self):
        return self.salario * self.BONUS


class Gerente(Funcionario):
    BONUS = 0.15

    @property
    def bonus(self):
        return self.salario * self.BONUS


#35 Crie um simulador que gerencie  a abertura de diferentes tipos de arquivos
class Arquivo(ABC):
    def __init__(self, nome, tamanho, extensao):
        self.nome = nome
        self.tamanho = tamanho
        self._extensao = extensao
        
    @property
    def nome_completo(self):
        return f'{self.nome}{self._extensao}'

    def abrir(self):
        return f'Abrindo arquivo {self.nome_completo} de {self.tamanho}MB no {self.app}'


class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, '.pdf')
        self.app = 'Microsof Word'


class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, '.doc')
        self.app = 'Google Sheets'


class PNG(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, '.png')
        self.app = 'Galeria de Fotos'


def abrir_arquivo(other):
    try:
        return other.abrir()
    except:
        print(f'Não foi possivel abrir o arquivo {other.__class__.__name__}')


#36 Crie um simulador que gerencie pagamentos em diferentes tipos
class Pagamento(ABC):
    def __init__(self):
        self._valor: int | float = 0

    @property
    def valor(self) -> int | float:
        return self._valor
    @valor.setter
    def valor(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError('Não é possivel realizar pagamento inferior ou igual a zero.')

        self._valor = value

    @property
    def fvalor(self) -> str:
        return locale.currency(self.valor, grouping=True)

    def pagar(self) -> str:
        return f'pagamento CONFIRMADO de {self.fvalor} no {self.__class__.__name__}'


class Pix(Pagamento):
    pass


class Debito(Pagamento):
    pass


class Credito(Pagamento):
    pass


def realizar_pagamento(metodo_pagamento: Pagamento, value: int | float) -> None:
    try:
        metodo_pagamento.valor = value
        print(metodo_pagamento.pagar())
    except ValueError as erro:
        print(erro)


#37 Implemente um sistema de mensagem padronizada usando POO.
class Mensagem:
    def __init__(self, mensagem: str, tipo: str = 'Aviso'):
        self._mensagem = mensagem
        self._tipo = tipo

    def mostrar(self) -> str:
        msg = []
        msg.append(f'{self._tipo:-^20}')
        msg.append(self._mensagem)

        return '\n'.join(msg)


class Erro(Mensagem):
    def __init__(self, mensagem: str):
        super().__init__(mensagem, 'Erro')



class Alerta(Mensagem):
    def __init__(self, mensagem: str):
        super().__init__(mensagem, 'Alerta')


#38 Implemente a sequinte estrutura com agregação, incluindo override operator (+) para adicionar produtos ao carrinho de compras
class Carrinho:
    def __init__(self):
        self.produtos: list[Produtos] = []

    def __add__(self, other: Produto | Carrinho):
        if isinstance(other, Produto):
            self.produtos.append(other)

        elif isinstance(other, Carrinho):
            self.produtos += other.produtos

        else:
            raise ValueError('Deixa de ser burro.')

        return self
    
    @property
    def total(self) -> int | float:
        total = 0
        for x in self.produtos:
            total += x.preço
        
        return total

    def __str__(self) -> str:
        msg: list = ['Carrinho de compras']
        msg.append('Produtos | Preços')
        
        for x in self.produtos:
            msg.append(f'{x.nome} {locale.currency(x.preço, grouping = True)}')
        
        msg.append(f'Total: {locale.currency(self.total, grouping = True)}')

        return '\n'.join(msg)

class Produto:
    def __init__(self, nome: str, preço: int | float):
        self.nome = nome
        self.preço = preço
   
39 Crie classes para validadores de dados, com os exemplos a seguir;
class Validador(ABC):
    @abstractmethod
    def validar(self, valor: str) -> str:
        pass
    
    @staticmethod
    def remover_espacos(valor: str) -> str:
        return valor.split()


class Usuario(Validador):
    MIN_CHAR = 5
    MAX_CHAR = 20

    def validar(self, valor: str) -> str:
        nome_list = self.remover_espacos(valor)
        nome = ' '.join(nome_list)
        nome_validar = ''.join(nome_list)
    
        if not nome_validar.isalpha():
            if '_' in nome_validar:
                if not nome_validar.replace('_', '').isalpha():
                    raise ValueError('Nome inválido, use apenas espaços ou underscore')
            else:
                raise ValueError('Nome inválido, use apenas espaços ou underscore')

        if not (self.MIN_CHAR <= len(nome) <= self.MAX_CHAR) or not (nome == nome.lower()):
            raise ValueError('Nome precisa ter de 5 a 20 caracteres, apenas minusculos.')

        return nome

class Email(Validador):
    def validar(self, valor: str) -> str:
        email = ''.join(self.remover_espacos(valor))
        if email.count('@') != 1 or not email.endswith('@') or not email.startswith('@') - 1] != '@'):
            raise ValueError('Endereço de email inválido.')

        if not ('.' in email[email.find('@'):]):
            raise ValueError('Email inválido')
        
        pos_ponto = email.rfind('.') + 1
        qtd_char = len(email[pos_ponto:])
        if not(2 <= qtd_char <= 3):
            raise ValueError('Final do email incorreto')

        return email 

class Senha(Validador):
    MIN_CHAR = 8

    def validar(self, valor: str) -> str:
        senha = ''.join(self.remover_espacos(valor))
        tamanho_senha = len(senha)
        is_letra_maiuscula = False 
        is_simbolo = senha.isalpha()

        for letter in senha:
            if letter.isupper():
                is_letra_maiuscula = True
                break

        if tamanho_senha < self.MIN_CHAR or not is_letra_maiuscula or is_simbolo:
            raise ValueError('Senha inválida')

        return senha

40 Implemente um exportador de dados funcional para JSON e XML
class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

    def to_dict(self) -> dict:
        return {'Nome': self.nome, 'Curso': self.curso, 'Serie': self.serie}

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def to_dict(self) -> dict:
        return {'Nome': self.nome, 'Email': self.email}


class JSON:
    @staticmethod
    def exportar(dados: list[ Aluno | Usuario ]):
        conteudo = [item.to_dict() for item in dados]

        with open('dados.json', 'w', encoding='utf-8') as arquivo:
            json.dump(conteudo, arquivo, indent=2)


class XML:
    @staticmethod
    def exportar(dados: list[ Aluno | Usuario ]):
        raiz = ET.Element('Dados')
        for other in dados:
            info = ET.SubElement(raiz, other.__class__.__name__)
            for chave, valor in other.to_dict().items():
                elem = ET.SubElement(info, chave)
                elem.text = str(valor)
        else:
            tree = ET.ElementTree(raiz)
            tree.write(f'{other.__class__.__name__}.xml')



