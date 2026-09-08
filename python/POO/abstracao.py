#Crie a classe Funcionário, onde podemos cadastrar o nome, setor e cargo. Crie tamme um método
# que permita ao funcionário se apresentar.
class Funcionario:
    def __init__(self, name, setor, cargo):
        self.name = name
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f'Olá me chamo {self.name}, trabalho no setor de {self.setor} no cargo de {self.cargo}.'

#17 Crie a classe produto, onde podemos cadastrar nome eo preço. Crie tamme um método que msotre
# uma etiqueta de preço do produto.
class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def etiqueta(self) -> str:
        cash = f'R${self.price:,.2f}'
        return f'{self.name:-^20}\n{cash:.^20}'

#18 Crie a classe churrasco, onde seja possivel informar quantas pessoas vão participar e mostre # quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa class Churrasco: consumo_padrao:float = 0.4 preço_padrão:float = 82.4

    def __init__(self, title, peoples):
        self.title = title
        self.peoples = peoples
        self.carne_kg = self.__class_.consumo_padrao * peoples
        self.price_total = self.carne_kg * self.__class__.preço_padrao
        self.price_person = self.price_total / peoples

    def info(self) -> str:
        return f'{self.title:^20}\nKg de carne: {self.carne_kg}\nCusto total: {self.price_total:.2f}\nCusto por pessoa: {self.price_person:.2f}'

#19 Crie a classe livro, que vai simular a pasagem de áginas de um livro, considerando taḿbém se o
# usuário chegou ao fim da leitura.
class Livro:
    def __init__(self, name, paginas):
        self.is_read = False
        self.name = name
        self.paginas = paginas
        self.pagina_atual = 1

    def next_page(self, qtd):
        if self.is_read:
            print('Leitura concluida')
            return

        for x in range(0, qtd):
            print(f'{self.pagina_atual} ->', end=' ')
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
            else:
                self.is_read = True
                break

        print(f'paǵina atual: {self.pagina_atual}')
        
        if self.is_read:
            print('Leitura concluída')

#20 Crie a classe games, onde podemos cadastrar nome, nick e o os jogos favoritos de uma pessoa.
# Crie um método que posso mostrar a ficha desse jogador
class Gamer:
    def __init__(self, name, nick, *games):
        self.name = name
        self.nick = nick
        self.games = list(games)
        
    def ficha(self) -> str:
        return f'Nome: {self.name}\nNickname: {self.nick}\nJogos Favoritos:\n{self.jogos()}'
    
    def jogos(self) -> str:
        games_list_str = []
        for game in self.games:
            games_list_str.append(f'{game}')
        return '\n'.join(games_list_str)

#21 Crie a classe caneta , que simule o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.
class Caneta:
    def __init__(self, color):
        self.tampa:bool = True
        self.color:str = color
        self.colors:dict = {
                'red': "\033[1;31m",
                'green': "\033[1;32m",
                'blue': "\033[1;34m",
                'cyan': "\033[1;36m",
                }

    def write(self, phrase):
        if not self.tampa:
            print(f'{self.colors.get(self.color) + phrase}', end=' ')
    
    def wrap(self, qtd = 0):
        print('\n' * qtd)

    def destampar(self):
        self.tampa = False

    def tampar(self):
        self.tampa = True

#22 Crie uma classe controle remoto, onde vamos simular o funcionamento de um controle simples
# (canal, volume e liga e desliga)
class ControleRemoto:
    def __init__(self):
        self.on_off = False
        self.channel = 1
        self.volume = 1
    
    def power_on(self):
        if not self.on_off:
            self.on_off = True
            self.channel = 1
            self.volume = 2
            self.display()
        else:
            self.on_off = False
            self.display()

    def display(self):
        if self.on_off:
            print('-' * 20)
            print('TV LIGADA')
            print('< Canais >', end=' ')
            for x in range(1, 6):
                if x == self.channel:
                    print(f'\33[32;47m {x} \33[0m', end=' ')
                    continue
                print(f' {x} ', end=' ')
            print()
            vol = f'\n- Volume + '
            for x in range(0, 5):
                if x < self.volume:
                    vol += f'\33[42m  \33[0m'
                else:
                    vol += f'\33[47m  \33[0m'
            print(vol)
        else:
            print('-' * 20)
            print('TV DESLIGADA')
            print('\n' * 2)

    def change_channel(self, foward_next):
        match foward_next:
            case '<':
                self.channel -= 1
                if self.channel < 1:
                    self.channel = 5
            case '>':
                self.channel += 1
                if self.channel > 5:
                    self.channel = 1

        self.display()

    def change_volume(self, inc_dec):
        match inc_dec:
            case '-':
                self.volume -= 1 
                if self.volume < 0:
                    self.volume = 0
            case '+':
                self.volume += 1
                if self.volume > 5:
                    self.volume = 5
        self.display()
        
    def control_init(self):
        while True:
            buttons_control = input('Controle Remoto: ')
            if buttons_control == 'q':
                break
        
            match buttons_control:
                case '@':
                    self.power_on()
                case '<':
                    self.change_channel('<')
                case '>':
                    self.change_channel('>')
                case '-':
                    self.change_volume('-')
                case '=':
                    self.change_volume('+')


