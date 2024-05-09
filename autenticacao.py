import csv

def menu_inicial():
    print("Bem vindo!")
    print("Digite uma opção para começar:")
    print("  1. Cadastrar")
    print("  2. Autenticar")
    print("  3. Sair")

    op = input("Opção:")
    
    #cadastrar
    if op == "1":
        usuario = input("Usuário: ")
        senha = input("Senha: ")

    #autenticar
    if op == "2":
        cadastra()
         
    #sair
    if op == "3":
        print("Tchau! :]") 

def cadastra():
    with open("usuarios.txt", "r") as usuarios:
        print("Atenção: as credenciais devem ter no máximo 4 caracteres!")
        usuario = input("Crie um usuário: ")
        senha = input("Crie uma senha: ")

        d = []
        f = []
        for i in usuarios:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        credenciais = dict(zip(d,f))

        if len(senha or usuario)>4:
            print("Atenção: as credenciais devem ter no máximo 4 caracteres!")
            cadastra()
        elif usuario in d:
                print("Usuário já existe! :(")
                cadastra()
        else: 
            with open("usuarios.txt", "a") as usuarios:        
                usuarios.write(usuario + ", " + senha + "\n")
                print("Novo usuário cadastrado!")
        
def autentica():

    with open("usuarios.txt", "r") as usuarios:

        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if not len(usuario or senha)<1:
            d = []
            f = []
            for i in usuarios:
                a,b = i.split(", ")
                b = b.strip()
                d.append(a)
                f.append(b)
            credenciais = dict(zip(d,f))