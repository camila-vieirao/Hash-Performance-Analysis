from autenticacao import menu_inicial
from autenticacao import comandos_disponiveis
if __name__ == '__main__':
    usuario = menu_inicial()
    comandos_disponiveis(usuario)