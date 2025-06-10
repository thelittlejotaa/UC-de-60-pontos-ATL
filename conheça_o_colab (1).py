# Lista de usuários cadastrados
usuarios = [
    {"usuario": "jota", "senha": "1234"},
    {"usuario": "guigui", "senha": "samurainocoliseu"},
    {"usuario": "frança", "senha": "psgchnpion"}
]

# Produtos disponíveis
produtos_disponiveis = {
    1: {"nome": "Tênis de Corrida Nike", "preco": 299.99},
    2: {"nome": "Camiseta Adidas", "preco": 79.99},
    3: {"nome": "Bola de Futebol Penalty", "preco": 99.99}
}

# Carrinho de compras (individual por sessão)
carrinho = []

# --- Funções de autenticação ---
def autenticar(usuario, senha):
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            return True
    return False

def login():
    while True:
        print("\n=== Login ===")
        print("1. Entrar")
        print("2. Criar novo usuário")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            if autenticar(usuario, senha):
                print(f"\n✅ Bem-vindo, {usuario}!")
                return usuario
            else:
                print("❌ Usuário ou senha incorretos.")
        elif escolha == "2":
            novo_usuario = input("Escolha um nome de usuário: ")
            if any(u["usuario"] == novo_usuario for u in usuarios):
                print("❌ Este nome de usuário já está em uso.")
            else:
                nova_senha = input("Digite uma senha: ")
                usuarios.append({"usuario": novo_usuario, "senha": nova_senha})
                print("✅ Usuário criado com sucesso! Faça login para continuar.")
        elif escolha == "3":
            return None
        else:
            print("❌ Opção inválida.")

def logout(usuario):
    if usuario:
        print(f"\n👋 Usuário {usuario} saiu. Até logo!")
    else:
        print("⚠️ Nenhum usuário logado.")

# --- Funções do carrinho ---
def adicionar_item(id_produto, quantidade):
    if id_produto in produtos_disponiveis:
        produto = produtos_disponiveis[id_produto]

        for item in carrinho:
            if item["nome"] == produto["nome"]:
                item["quantidade"] += quantidade
                print(f"{quantidade}x {produto['nome']} adicionados ao carrinho. Total: {item['quantidade']}.")
                return

        carrinho.append({"nome": produto["nome"], "quantidade": quantidade, "preco": produto["preco"]})
        print(f"{quantidade}x {produto['nome']} adicionado ao carrinho.")
    else:
        print("❌ Produto não encontrado.")

def remover_item(nome):
    for item in carrinho:
        if item["nome"].lower() == nome.lower():
            if item["quantidade"] > 1:
                item["quantidade"] -= 1
                print(f"Uma unidade de {nome} removida. Restam {item['quantidade']}.")
            else:
                carrinho.remove(item)
                print(f"{nome} removido do carrinho.")
            return
    print("❌ Item não encontrado no carrinho.")

def mostrar_carrinho():
    if not carrinho:
        print("🛒 Carrinho vazio.")
        return

    print("\n--- Carrinho de Compras ---")
    for i, item in enumerate(carrinho, 1):
        print(f"{i}. {item['nome']} - {item['quantidade']} x R${item['preco']:.2f} = R${item['quantidade'] * item['preco']:.2f}")
    print(f"Total: R${calcular_total():.2f}")

def calcular_total():
    return sum(item["quantidade"] * item["preco"] for item in carrinho)

def finalizar_compra():
    if not carrinho:
        print("⚠️ Seu carrinho está vazio.")
        return

    print("\n🧾 Finalizando compra...")
    mostrar_carrinho()

    metodos_pagamento = ["PIX", "Cartão de Crédito", "Boleto Bancário"]
    metodo = None

    while metodo not in metodos_pagamento:
        print("\nEscolha um método de pagamento:")
        for i, m in enumerate(metodos_pagamento, 1):
            print(f"{i}. {m}")
        opcao = input("Digite o número do método de pagamento: ")

        if opcao.isdigit() and 1 <= int(opcao) <= len(metodos_pagamento):
            metodo = metodos_pagamento[int(opcao) - 1]
        else:
            print("❌ Opção inválida. Tente novamente.")

    print(f"\n✅ Compra finalizada com pagamento via {metodo}. Obrigado pela preferência!")
    carrinho.clear()  # Esvaziar carrinho após finalização

# --- Menu principal do sistema ---
def menu():
    while True:
        print("\n📦 Produtos disponíveis:")
        for id_produto, produto in produtos_disponiveis.items():
            print(f"{id_produto}. {produto['nome']} - R${produto['preco']:.2f}")

        print("\n📋 Menu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Mostrar carrinho")
        print("4. Finalizar compra")
        print("5. Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id_produto = int(input("Digite o número do produto: "))
                qtd = int(input("Quantidade: "))
                adicionar_item(id_produto, qtd)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcao == "2":
            nome = input("Nome do produto para remover: ")
            remover_item(nome)
        elif opcao == "3":
            mostrar_carrinho()
        elif opcao == "4":
            finalizar_compra()
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida.")

# --- Execução principal ---
usuario_logado = login()
if usuario_logado:
    menu()
    logout(usuario_logado)
else:
    print("\nPrograma encerrado.")


