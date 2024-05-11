def menu_inicial():

    while True:
        print("Bem vindo!")
        print("Digite uma opção para começar:")
        print("  1. Cadastrar")
        print("  2. Autenticar")
        print("  3. Sair")

        op = input("\nOpção:")
        
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
                    print("Usuário já existe! :(\n")

        #autenticar
        elif op == "2":
            usuario = input("Usuário: ")
            senha = input("Senha: ")

            auth = autentica(usuario, senha)

            if auth:
                print("\nUsuário autenticado!")
                print("Olá, " + usuario)
                return usuario
            elif auth == None:
                print("Usuário não existe! :c")
            else:
                print("Falha na autenticação! :c")
            
        #sair
        elif op == "3":
            print("Tchau! :]")
            break

        else: 
            print("Opção não existe! :c")

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
            lista_arquivos()


        # 2- Criar arquivo

        elif op == "2":
            cria_arquivo()


        # 3- Ler arquivo

        elif op == "3":
            le_arquivo()


        # 4- Excluir arquivo

        elif op == "4":
            exclui_arquivo()


        # 5- Executar arquivo

        elif op == "5":
            executa_arquivo()


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

            
            