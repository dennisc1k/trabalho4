import os

# Etapa 2: Exceção personalizada
class ProductNotFoundError(Exception):
    """Exceção personalizada para produto não encontrado no inventário."""
    def __init__(self, nome_produto):
        super().__init__(f"Erro: Produto '{nome_produto}' não encontrado no inventário.")

# Etapa 1: Classe base Produto
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} | Preço: R${self.preco:.2f}"

# Etapa 1: Subclasse Eletrônico
class Eletronico(Produto):
    def __init__(self, nome: str, preco: float, garantia_meses: int):
        super().__init__(nome, preco)
        self.garantia_meses = garantia_meses

    def __str__(self):
        return f"{self.nome} | Preço: R${self.preco:.2f} | Garantia: {self.garantia_meses} meses"

# Etapa 1: Subclasse Comida
class Comida(Produto):
    def __init__(self, nome: str, preco: float, data_validade: str):
        super().__init__(nome, preco)
        self.data_validade = data_validade

    def __str__(self):
        return f"{self.nome} | Preço: R${self.preco:.2f} | Validade: {self.data_validade}"

# Etapa 3: Classe Inventário
class Inventario:
    def __init__(self):
        self.__produtos = []  # Composição e encapsulamento

    def add_product(self, produto):
        self.__produtos.append(produto)

    def remove_product(self, product_name):
        for produto in self.__produtos:
            if produto.nome == product_name:
                self.__produtos.remove(produto)
                print(f"Produto '{product_name}' removido com sucesso.")
                return
        raise ProductNotFoundError(product_name)

    def list_products(self):
        print("=== Sistema de Inventário ===")
        print("--- Produtos no Estoque ---")
        if not self.__produtos:
            print("Nenhum produto no inventário.")
        else:
            for produto in self.__produtos:
                print(produto)
        print("----------------------------")

    def get_product(self, product_name):
        for produto in self.__produtos:
            if produto.nome == product_name:
                return produto
        raise ProductNotFoundError(product_name)

# Etapa 4: Código principal com menu interativo
def main():
    inventario = Inventario()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Sistema de Inventário ===")
        print("--- Menu Principal ---")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Sistema de Inventário ===")
            print("--- Adicionar Produto ---")
            tipo = input("Tipo (eletronico/comida): ").strip().lower()
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            if tipo == "eletronico":
                garantia = int(input("Garantia (meses): "))
                produto = Eletronico(nome, preco, garantia)
            elif tipo == "comida":
                validade = input("Data de validade (AAAA-MM-DD): ")
                produto = Comida(nome, preco, validade)
            else:
                print("Tipo inválido.")
                input("Pressione Enter para continuar...")
                continue
            inventario.add_product(produto)
            print("Produto adicionado com sucesso.")
            input("Pressione Enter para continuar...")

        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Sistema de Inventário ===")
            print("--- Remover Produto ---")
            nome = input("Nome do produto a remover: ")
            try:
                inventario.remove_product(nome)
            except ProductNotFoundError as e:
                print(e)
            input("Pressione Enter para continuar...")

        elif opcao == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            inventario.list_products()
            input("Pressione Enter para continuar...")

        elif opcao == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Sistema de Inventário ===")
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

# Executa o programa
main()
