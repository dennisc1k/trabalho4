import os

class ProductNotFoundError(Exception):
    def __init__(self, identificador):
        super().__init__(f"Erro: Produto com ID '{identificador}' não encontrado no inventário.")

class Produto:
    _id_counter = 1  # contador de ID único

    def __init__(self, nome: str, preco: float):
        self.id = Produto._id_counter
        Produto._id_counter += 1
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'ID: {self.id} | {self.nome} | Preço: R${self.preco:.2f}'

class Eletronico(Produto):
    def __init__(self, nome: str, preco: float, garantia_meses: int):
        super().__init__(nome, preco)
        self.garantia_meses = garantia_meses

    def __str__(self):
        return f'ID: {self.id} | {self.nome} | Preço: R${self.preco:.2f} | Garantia: {self.garantia_meses} meses'

class Comida(Produto):
    def __init__(self, nome: str, preco: float, data_validade: str):
        super().__init__(nome, preco)
        self.data_validade = data_validade

    def __str__(self):
        return f'ID: {self.id} | {self.nome} | Preço: R${self.preco:.2f} | Validade: {self.data_validade}'

class Inventario:
    def __init__(self):
        self.__produtos = []

    def add_product(self, produto):
        self.__produtos.append(produto)

    def remove_product(self, product_id):
        for produto in self.__produtos:
            if produto.id == product_id:
                self.__produtos.remove(produto)
                print(f"Produto com ID '{product_id}' removido com sucesso.")
                return
        raise ProductNotFoundError(product_id)

    def buscar_por_id(self, product_id):
        for produto in self.__produtos:
            if produto.id == product_id:
                return produto
        raise ProductNotFoundError(product_id)

    def list_products(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== Sistema de Inventário ===')
        print('--- Produtos no Estoque ---')
        if not self.__produtos:
            print('Nenhum produto no inventário.')
        else:
            for produto in self.__produtos:
                print(produto)
        print('----------------------------')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=== Sistema de Inventário ===')
    print('Bem-vindo ao sistema de inventário!')
    inventario = Inventario()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== Sistema de Inventário ===')
        print('--- Menu Principal ---')
        print('1. Adicionar Produto')
        print('2. Remover Produto por ID')
        print('3. Listar Produtos')
        print('4. Buscar Produto por ID')
        print('5. Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- Adicionar Produto ---')
            tipo = input('Tipo (eletronico/comida): ').strip().lower()
            nome = input('Nome do produto: ')
            preco = float(input('Preço: '))
            if tipo == 'eletronico':
                garantia = int(input('Garantia (meses): '))
                produto = Eletronico(nome, preco, garantia)
            elif tipo == 'comida':
                validade = input('Data de validade (AAAA-MM-DD): ')
                produto = Comida(nome, preco, validade)
            else:
                print('Tipo inválido.')
                input('Pressione Enter para continuar...')
                continue
            inventario.add_product(produto)
            print(f'Produto adicionado com sucesso. ID: {produto.id}')
            input('Pressione Enter para continuar...')
        elif opcao == '2':
            print('--- Remover Produto por ID ---')
            try:
                product_id = int(input('ID do produto a remover: '))
                inventario.remove_product(product_id)
            except ValueError:
                print('ID inválido.')
            except ProductNotFoundError as e:
                print(e)
            input('Pressione Enter para continuar...')
        elif opcao == '3':
            inventario.list_products()
            input('Pressione Enter para continuar...')
        elif opcao == '4':
            print('--- Buscar Produto por ID ---')
            try:
                product_id = int(input('ID do produto: '))
                produto = inventario.buscar_por_id(product_id)
                print('Produto encontrado:')
                print(produto)
            except ValueError:
                print('ID inválido.')
            except ProductNotFoundError as e:
                print(e)
            input('Pressione Enter para continuar...')
        elif opcao == '5':
            print('Obrigado por usar o Faststock. Até logo!')
            break
        else:
            print('Opção inválida.')
            input('Pressione Enter para continuar...')

main()
