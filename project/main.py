from autenticacao import menu_inicial
from autenticacao import lista_arquivos
if __name__ == '__main__':
    usuario = menu_inicial()
    lista_arquivos(usuario)