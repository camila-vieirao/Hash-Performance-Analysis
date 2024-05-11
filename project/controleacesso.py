import os

def lista_arquivos(usuario):
    with open("project/permissoes.txt", "r") as arquivos:

        for linha in arquivos:
            perm_usuario, arquivo, r, w, x = linha.strip().split(", ")
            if perm_usuario == usuario and r == '1':
                print("-", arquivo)

def cria_arquivo(usuario, novo_arquivo):
    with open("project/permissoes.txt", "a") as arquivos:
        arquivos.write(usuario + ", " + novo_arquivo + ", 1, 1, 1\n")
    return True

def le_arquivo(usuario, nome_arquivo):
    with open("project/permissoes.txt", "r") as arquivos:

        for linha in arquivos:
            perm_usuario, arquivo, r, w, x = linha.strip().split(", ")
            if nome_arquivo not in arquivos:
                return None
            elif perm_usuario == usuario and arquivo == nome_arquivo and r == "1":
                return True
            else:
                return False
            
def exclui_arquivo(usuario, nome_arquivo):
    with open("project/permissoes.txt", "w") as arquivos:

        for linha in arquivos:
            perm_usuario, arquivo, r, w, x = linha.strip().split(", ")
            if nome_arquivo not in arquivos:
                return None
            elif perm_usuario == usuario and arquivo == nome_arquivo and all(p == "1" for p in [r, w, x]):
                os.remove(nome_arquivo)
                return True
            else:
                return False
            

def executa_arquivo(usuario, nome_arquivo):
    with open("project/permissoes.txt", "r") as arquivos:

        for linha in arquivos:
            perm_usuario, arquivo, r, w, x = linha.strip().split(", ")
            if nome_arquivo not in arquivos:
                return None
            elif perm_usuario == usuario and arquivo == nome_arquivo and x == "1":
                return True
            else:
                return False