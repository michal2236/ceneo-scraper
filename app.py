import json
from productScraper import ProductScraper
from product import Product
from flask import Flask, render_template

#product_id = '103735237'
#96092975 - hulajnoga xiaomi
#103735237 - telewizor

app = Flask(__name__, template_folder="templates")

stored_products = {}

@app.route("/")
def homePage():
    return render_template('homepage/homepage.html')

@app.route("/extraction")
def extractionPage():
    return render_template('extraction/extraction.html')

@app.route("/product/<productId>")
def productPage(productId):
    product_scraper = ProductScraper(productId)
    product = Product(productId, product_scraper.get_product_name(), product_scraper.get_product_opinions())
    stored_products.update(product.get_product_jsonable_object())
    #with open('opinions.json', 'w') as jsonfile:
    #    json.dump(stored_products, jsonfile, indent=4)
    return render_template('product/product.html', opinions=product.get_product_opinions(), productId=productId)

@app.route("/product/<productId>/statistics")
def productStatisticsPage(productId):
    global product_opinions
    product_opinions = stored_products[productId]['opinions']
    return render_template('statistics/statistics.html', opinions=product_opinions, productId=productId)

@app.route("/product-list")
def productListPage():
    global products
    products = stored_products
    return render_template('product-list/product-list.html', storedProducts=products)

if __name__ == '__main__':
    app.run()