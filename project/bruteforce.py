import hashlib
import time

def bruteforce(senhas):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    tam_max_senha = 4 
    tempo_total = 0

    for usuario, senha_hash in senhas:
        print(f"Tentando quebrar a senha para o usuário {usuario}...")
        start_time = time.time() 
        for tam_senha in range(1, tam_max_senha + 1):
            tempo = time.time() 
            if attempt_bruteforce(usuario, senha_hash, caracteres, '', tam_senha):
                tempo_total += time.time() 
                break  

    print(f"Tempo total para quebrar todas as senhas: {tempo_total:.2f} segundos")

def attempt_bruteforce(usuario, senha_hash, caracteres, current_password, tam_senha):
    if tam_senha == 0:
        hashed_password = hashlib.sha256(current_password.encode()).hexdigest()
        if hashed_password == senha_hash:
            print(f"A senha para o usuário {usuario} foi encontrada: {current_password}")
            return True
    else:
        for char in caracteres:
            if attempt_bruteforce(usuario, senha_hash, caracteres, current_password + char, tam_senha - 1):
                return True

    return False

def obter_senhas():
    with open("project/usuarios.txt", "r") as arquivo:
        senhas = []
        for linha in arquivo:
            usuario, senha_hash = linha.strip().split(", ")
            senhas.append((usuario, senha_hash))
    return senhas

def main():
    senhas = obter_senhas()
    bruteforce(senhas)

if __name__ == "__main__":
    main()