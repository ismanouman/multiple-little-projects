class UtilityStoreBackend:
    def __init__(self):
        self.users = []
        self.products = []

    def register_user(self, username, password):
        self.users.append({'username': username, 'password': password})

    def add_product(self, product_name, price):
        product_id = len(self.products) + 1
        self.products.append({'id': product_id, 'name': product_name, 'price': price, 'stock': 0})

    def sell_product(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product and product['stock'] >= quantity:
            product['stock'] -= quantity
            return True
        return False

    def purchase_product(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product:
            product['stock'] += quantity

    def generate_report(self, report_type):
        # Generate and return reports based on report_type
        # Implement your report generation logic here
        pass

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None
