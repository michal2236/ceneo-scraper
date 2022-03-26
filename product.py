class Product:
    def __init__(self, product_id, product_name, product_opinions):
        self.product_id = product_id
        self.product_name = product_name
        self.product_opinions = product_opinions

    def get_product_opinions(self):
        return self.product_opinions

    def get_product_jsonable_object(self):
        product_object = {}
        product_object[self.product_id] = {}
        product_object[self.product_id]['name'] = self.product_name
        product_object[self.product_id]['opinions'] = self.product_opinions
        return product_object

    