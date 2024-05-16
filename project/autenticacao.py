from hashlib import sha256
import random
import string
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
                senha_salted, sal = salt(senha)
                if cadastra(usuario, senha_salted, sal):
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
            exit(0)

        else: 
            print("\nOpção não existe! :c")

def cadastra(usuario, senha, salts):

    with open("project/usuarios.txt", "r") as usuarios:

        usu = []
        sen = []
        sal = []
        for i in usuarios:
            a,b,c = i.split(", ")
            c = c.strip()
            usu.append(a)
            sen.append(b)
            sal.append(c)


    if usuario in usu:
        return False
    else: 
        with open("project/usuarios.txt", "a") as usuarios:        
            usuarios.write(usuario + ", " + senha + ", " + salts + "\n")
    return True
        
def autentica(usuario, senha):

    with open("project/usuarios.txt", "r") as usuarios:

        if not len(usuario or senha)<1:
            usu = []
            sen = []
            sal = []
            for i in usuarios:
                a,b,c = i.split(", ")
                c = c.strip()
                usu.append(a)
                sen.append(b)
                sal.append(c)


        if usuario not in usu:
            return None
        
        i = usu.index(usuario)

        senha_salt = senha + sal[i]
        senha_hash = sha256(senha_salt.encode()).hexdigest()
        if sen[i] != senha_hash:
            return False
        
        return True
    
def salt(senha):
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    salted = senha + salt
    return sha256(salted.encode()).hexdigest(), salt
