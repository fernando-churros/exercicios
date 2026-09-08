# 23 Implemente o seguinte diagrama: Poligono abstract | +qtd_lados | perimetro() abstract | area() abstract

from abc import ABC, abstractmethod
from random import randint, random, uniform
from math import trunc

class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados:int = lados
    
    @abstractmethod
    def perimetro() -> float:
        pass

    @abstractmethod
    def area() -> float:
        pass

class Quadrado(Poligono):
    def __init__(self, tam_lado):
        super().__init__(4)
        self.tam_lado:int = tam_lado
    
    def perimetro(self) -> float:
        return 4 * self.tam_lado

    def area(self) -> float:
        return self.tam_lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        self.raio:int = raio
        self.PI:float = 3.14159

    def perimetro(self) -> float:
        return 2 * self.PI * self.raio

    def area(self) -> float:
        return self.PI * self.raio ** 2


#24 Simule uma cafeteira orientada a objetos
class BebidaQuente(ABC):
    def preparar(self):
        preparo = []
        preparo.append(f'{" Iniciando Preparo ":-^25}')
        preparo.append(self.ferver_agua())
        preparo.append(self.misturar())
        preparo.append(self.servir())
        preparo.append(f'{" Bebida Pronta ":-^25}')
    
        return '\n'.join(preparo)

    def ferver_agua(self):
        return f'Fervendo água a 100 graus celsius'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        pass

    def misturar(self):
        return f'Passando água pressurizada pelo pó de café moido'

    def servir(self):
        return f'Servindo em um chicára pequena'


class Cha(BebidaQuente):
    def misturar(self):
        return f'Mergulhando o sachê de ervas na água'

    def servir(self):
        return f'Servindo na caneca de porcelana com limão'

class Leite(BebidaQuente):
    def misturar(self):
        return f'Passando vapor pressurizado pelo bico do leite'

    def servir(self):
        return f'Servindo na caneca grande, já com café'


#25 Crie classes para calcular fretes para veiculos diferentes: moto 0.5 | caminhão 1.2 | drone 9.50
class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
        self.calc_frete()

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator:float = 0.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self) -> str:
        self.frete = self.distancia * self.fator
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    fator:float = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self) -> str:
        if self.distancia < 50:
            return f'Distância miníma para o frete é de 50Km'

        self.frete = self.distancia * self.fator
        return f'R${self.frete:.2f}'


class Drone(Transporte):
    fator:float = 9.5

    def __init__(self, distancia):
        super().__init__(distancia)


    def calc_frete(self):
        if self.distancia > 10:
            return f'Distância máxima é de 10km'

        self.frete = self.distancia * self.fator
        return f'R${self.frete:.2f}'

dist = 80
#viagens = [Moto(dist), Caminhao(dist), Drone(dist)]

#conteudo = []
#conteudo.append(f'{"Distancia":<10}|{"Veículo":<10}|{"Valor":<10}')
#for viagem in viagens:
#    conteudo.append(f'{dist:<10}|{type(viagem).__name__:<10}|{viagem.calc_frete():<10}')

#26 Crie uma estrutura capaz de calcular sálarios de diferentes funcionários.
class Funcionario(ABC):
    sal_minimo = 1612
    inss = 0.075

    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.sal_liquido = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        return f'Funcionário: {self.nome}, Salário Bruto: R${self.sal_bruto:.2f}, Salário Líquido: R${self.sal_liquido:.2f}. Corresponde a {self.sal_liquido / self.sal_minimo:.1f} salários minimos'

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.calc_sal()
    
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.sal_liquido = self.sal_bruto * (1 - self.inss)


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
        self.calc_sal()

    def calc_sal(self):
        self.sal_liquido = self.sal_bruto * (1 - self.inss)

h1 = Horista('fernando', 14, 36)
m1 = Mensalista('Sidney', 4200)

print(h1.analisar_sal())
print(m1.analisar_sal())


#27 Simule o sistema de batalha entre personagens de um rpg
class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, força):
        ataque_aleatorio = randint(0, len(self.golpes) - 1)
        força_ataque = randint(0, força)

        print(f'{type(self).__name__} usou {self.golpes[ataque_aleatorio]}')
        alvo.receber_dano(força_ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f'Dano: {dano}, Vida: {self.vida}')
        
    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, golpes=['Corte Crescente', 'Lua Aspiral'])

    def curar(self):
        cura_realizada = randint(0, 50)
        self.vida += cura_realizada
        print(f'{type(self).__name__} se curou {cura_realizada}')

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=60, golpes=['Flecha de Gele', 'Rajada de Luz'])

    def curar(self):
        if self.vida < 45:
            self.vida += 10
            print(f'+10 | vida: {self.vida}')
        else:
            print('Cura indisponivel')

p1 = Guerreiro('Leonidas')
p2 = Arqueiro('Ymir')

p2.atacar(p1, 95)
p1.curar()

