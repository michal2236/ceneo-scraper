class ProductsStore:
    def __init__(self):
        self.stored_products = {}
    
    def append_product(self, product_jsonable_object):
        self.stored_products.update(product_jsonable_object)
    
    def get_stored_products(self):
        return self.stored_products

    def get_stored_product(self, product_id):
        return self.stored_products[product_id]

    def get_converted_for_product_list(self):
        converted_products = []
        for product in self.stored_products.items():
            converted_product = {}
            converted_product['id'] = product[0]
            converted_product['name'] = product[1]['name']
            converted_product['opinionsCount'] = len(product[1]['opinions'].keys())
            converted_product['positivesCount'] = sum(map(lambda opinion: len(opinion['positives']), product[1]['opinions'].values()))
            converted_product['negativesCount'] = sum(map(lambda opinion: len(opinion['negatives']), product[1]['opinions'].values()))
            product_rates = list(map(lambda opinion: float(opinion['postScoreCount'].split('/')[0].replace(',', '.')), product[1]['opinions'].values()))
            converted_product['averageRating'] = round(sum(product_rates) / len(product_rates),1) if len(product_rates) > 0 else 0
            converted_products.append(converted_product)
        return converted_products
    