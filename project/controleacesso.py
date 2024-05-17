#Camila Vieira de Oliveira
import os

def comandos_disponiveis(usuario):
    while True:
        print("\nComandos disponíveis:")
        print("  1. Listar arquivos")
        print("  2. Criar arquivo")
        print("  3. Ler arquivo")
        print("  4. Excluir arquivo")
        print("  5. Executar arquivo")
        print("  6. Sair")

        op = input("\nOpção: ")    


        # 1- Listar arquivos

        if op == "1":
            print("\nArquivos no diretório: ")
            lista_arquivos(usuario)


        # 2- Criar arquivo

        elif op == "2":
            
            novo_arquivo = input("\nDigite o nome do arquivo que deseja criar: ")
            adicionar = cria_arquivo(usuario, novo_arquivo)
            if adicionar:
                print("Arquivo criado com sucesso!")
            elif adicionar == False:
                print("Este diretório já possui um arquivo com este nome.")

        # 3- Ler arquivo

        elif op == "3":
            nome_arquivo = input("\nDigite o nome do arquivo que deseja ler: ")
            ler = le_arquivo(usuario, nome_arquivo)
            if ler:
                print("\nArquivo ",  nome_arquivo, "lido!")
            elif ler == False:
                print("\nNão é possível ler o arquivo! :c")

        # 4- Excluir arquivo

        elif op == "4":
            nome_arquivo = input("\nDigite o nome do arquivo que deseja excluir: ")
            excluido = exclui_arquivo(usuario, nome_arquivo)
            if excluido:
                print("\nArquivo ",  nome_arquivo, "excluído!")
            elif excluido == False:
                print("\nNão é possível excluir o arquivo! :c")


        # 5- Executar arquivo

        elif op == "5":
            nome_arquivo = input("\nDigite o nome do arquivo que deseja executar: ")
            execu = executa_arquivo(usuario, nome_arquivo)
            if execu:
                print("\nArquivo ",  nome_arquivo, "executado!")
            elif execu == False:
                print("\nNão é possível executar o arquivo! :c")


        # 6- Sair

        elif op == "6":
            print("Tchau! :]")
            break

        else:
            print("Opção não existe! :c")
            
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
            if perm_usuario == usuario and arquivo == nome_arquivo and r == "1":
                return True
        return False
            
def exclui_arquivo(usuario, nome_arquivo):
    linhas = []
    removido = False

    with open("project/permissoes.txt", "r+") as arquivos:
        linhas = arquivos.readlines() 

        arquivos.seek(0)

        for linha in linhas:
            perm_usuario, arquivo, r, w, x = linha.strip().split(", ")
            if perm_usuario == usuario and arquivo == nome_arquivo and all(p == "1" for p in [r, w, x]):
                removido = True 
            else:
                arquivos.write(linha) # se nao for removido, vai escrever a linha novamente

        arquivos.truncate()

    return removido 

def executa_arquivo(usuario, nome_arquivo):
    with open("project/permissoes.txt", "r") as arquivos:

        for linha in arquivos:
            perm_usuario, arquivo, r, w, x = linha.strip().split(", ")
            if perm_usuario == usuario and arquivo == nome_arquivo and x == "1":
                return True
        return False