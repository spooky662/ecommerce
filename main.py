from store import Store
from cart import Cart

store = Store()
cart = Cart()

def menu():
    while True:
        print("\n=== Mini Mercado ===")
        print("1. Ver produtos")
        print("2. Comprar produto")
        print("3. Ver carrinho")
        print("0. Sair")

        choice = input("Escolha: ")

        if choice == "1":
            store.list_products()
        elif choice == "2":
            try:
                id = int(input("Digite o ID do produto: "))
                product = store.get_product_by_id(id)
                if product:
                    cart.add(product)
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("ID inválido.")
        elif choice == "3":
            cart.view()
        elif choice == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

menu()
