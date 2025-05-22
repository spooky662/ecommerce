class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        print(f"✅ {product.name} adicionado ao carrinho.")

    def view(self):
        if not self.items:
            print("🛒 Carrinho vazio.")
            return

        total = 0
        print("\n🛒 Seu Carrinho:")
        for item in self.items:
            print(f"- {item.name} - R${item.price:.2f}")
            total += item.price
        print(f"Total: R${total:.2f}")
