#Camila Vieira de Oliveira
from autenticacao import menu_inicial
from controleacesso import comandos_disponiveis
if __name__ == '__main__':
    usuario = menu_inicial()
    comandos_disponiveis(usuario)