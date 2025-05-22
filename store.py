from product import Product

class Store:
    def __init__(self):
        self.products = []
        self.load_products()

    def load_products(self):
        # Produtos fictícios
        self.products.append(Product(1, "Arroz", 5.99))
        self.products.append(Product(2, "Feijão", 4.49))
        self.products.append(Product(3, "Macarrão", 3.25))

    def list_products(self):
        for product in self.products:
            print(product)

    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None
