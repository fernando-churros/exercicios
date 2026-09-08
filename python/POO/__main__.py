from polimorfismo import *

def exportar_dados(extensao: JSON | XML, dados: list[ Usuario | Aluno ]):
    extensao.exportar(dados)

def main():
        
    exportar_dados(JSON(), u)
if __name__ == '__main__':
    main()

