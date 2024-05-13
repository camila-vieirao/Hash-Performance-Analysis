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
                senha_hash = sha256(senha.encode()).hexdigest() #calculando o hash para implementar no cadastra()
                if cadastra(usuario, senha_hash):
                    print("\nNovo usuário cadastrado!\n")
                else:
                    print("\nUsuário já existe! :(\n")

        #autenticar
        elif op == "2":
            usuario = input("\nUsuário: ")
            senha = input("Senha: ")

            senha_hash = sha256(senha.encode()).hexdigest()

            auth = autentica(usuario, senha_hash)

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
            exit(0)

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