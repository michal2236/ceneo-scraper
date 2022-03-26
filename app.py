import json
from productsStore import ProductsStore
from productScraper import ProductScraper
from product import Product
from flask import Flask, render_template, request

#product_id = '103735237'
#96092975 - hulajnoga xiaomi
#103735237 - telewizor

app = Flask(__name__, template_folder="templates")

products_store = ProductsStore()

@app.route("/")
def homePage():
    return render_template('homepage/homepage.html')

@app.route("/extraction")
def extractionPage():
    error = False
    if request.args.get('error'):
        error = request.args.get('error')
    return render_template('extraction/extraction.html', error=error)

@app.route("/product/<productId>")
def productPage(productId):
    product_scraper = ProductScraper(productId)
    if product_scraper.check_error():
        return render_template('product/product.html', opinions={}, error=True, productId=0)
    product = Product(productId, product_scraper.get_product_name(), product_scraper.get_product_opinions())
    error = False
    opinions = product.get_product_opinions()
    if len(opinions.keys()) == 0:
        error = True
    else:
        products_store.append_product(product.get_product_jsonable_object())
    return render_template('product/product.html', opinions=opinions, error=error, productId=productId)

@app.route("/product/<productId>/statistics")
def productStatisticsPage(productId):
    global product_opinions
    product_opinions = products_store.get_stored_product(productId)['opinions']
    return render_template('statistics/statistics.html', opinions=product_opinions, productId=productId)

@app.route("/product-list")
def productListPage():
    global products_list
    products_list = products_store.get_converted_for_product_list()
    return render_template('product-list/product-list.html', productsList=products_list)

@app.route("/get-opinions/<productId>")
def getOpinionsRequest(productId):
    global product
    product = products_store.get_stored_product(productId)
    return product['opinions']

@app.route("/author")
def getAuthorPage():
    return render_template('author/author.html')

if __name__ == '__main__':
    app.run()