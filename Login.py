usuarios = [
    {"usuario": "jota", "senha": "1234"},
    {"usuario": "guigui", "senha": "samurainocoliseu"},
    {"usuario": "frança", "senha": "psgchnpion"}
]

def autenticar(usuario, senha):
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            return True
    return False

def login():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if autenticar(usuario, senha):
        print("Bem-vindo,", usuario)
        return usuario
    else:
        print("Nome de usuário ou senha incorretos.")
        return None

def logout(usuario):
    if usuario:
        print("Usuário", usuario, "saiu")
    else:
        print("Nenhum usuário logado.")


usuario_logado = login()
logout(usuario_logado)
