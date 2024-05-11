from hashlib import sha256
from controleacesso import cria_arquivo, le_arquivo, lista_arquivos, exclui_arquivo, executa_arquivo

def menu_inicial():

    while True:
        print("Bem vindo!")
        print("Digite uma opção para começar:")
        print("  1. Cadastrar")
        print("  2. Autenticar")
        print("  3. Sair")

        op = input("\nOpção: ")
        
        #cadastrar
        if op == "1":
            usuario = input("\nCrie um usuário: ")
            senha = input("Crie uma senha: ")
            if len(senha) > 4 or len(usuario) > 4:
                print("\nAtenção: as credenciais devem ter no máximo 4 caracteres!\n")
            else:
                if cadastra(usuario, senha):
                    print("\nNovo usuário cadastrado!\n")
                else:
                    print("\nUsuário já existe! :(\n")

        #autenticar
        elif op == "2":
            usuario = input("\nUsuário: ")
            senha = input("Senha: ")

            auth = autentica(usuario, senha)

            if auth:
                print("\nUsuário autenticado!")
                print("Olá, " + usuario)
                return usuario
            elif auth == None:
                print("\nUsuário não existe! :c")
            else:
                print("\nFalha na autenticação! :c")
            
        #sair
        elif op == "3":
            print("Tchau! :]")
            break

        else: 
            print("\nOpção não existe! :c")

def cadastra(usuario, senha):

    with open("project/usuarios.txt", "r") as usuarios:

        d = []
        f = []
        for i in usuarios:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)


    if usuario in d:
        return False
    else: 
        with open("project/usuarios.txt", "a") as usuarios:        
            usuarios.write(usuario + ", " + senha + "\n")
    return True
        
def autentica(usuario, senha):

    with open("project/usuarios.txt", "r") as usuarios:

        if not len(usuario or senha)<1:
            d = []
            f = []
            for i in usuarios:
                a,b = i.split(", ")
                b = b.strip()
                d.append(a)
                f.append(b)


        if usuario not in d:
            return None
        
        i = d.index(usuario)

        if f[i] != senha:
            return False
        
        return True

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

        # 3- Ler arquivo

        elif op == "3":
            nome_arquivo = input("\nDigite o nome do arquivo que deseja ler: ")
            ler = le_arquivo(usuario, nome_arquivo)
            if ler:
                print("\nArquivo ",  nome_arquivo, "lido!")
            elif ler == None:
                print("\nArquivo não existe! :c")
            elif ler == False:
                print("\nNão é possível ler o arquivo! :c")

        # 4- Excluir arquivo

        elif op == "4":
            excluido = exclui_arquivo(usuario, nome_arquivo)
            if excluido:
                print("\nArquivo ",  nome_arquivo, "excluído!")
            elif ler == None:
                print("\nArquivo não existe! :c")
            elif ler == False:
                print("\nNão é possível excluir o arquivo! :c")


        # 5- Executar arquivo

        elif op == "5":
            exec = executa_arquivo(usuario, nome_arquivo)
            if exec:
                print("\nArquivo ",  nome_arquivo, "executado!")
            elif exec == None:
                print("\nArquivo não existe! :c")
            elif exec == False:
                print("\nNão é possível executar o arquivo! :c")


        # 6- Sair

        elif op == "6":
            print("Tchau! :]")
            break

        else:
            print("Opção não existe! :c")