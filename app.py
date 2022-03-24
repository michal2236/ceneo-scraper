import json
from scraper import Scraper
from flask import Flask, render_template

#product_id = '103735237'
#96092975 - hulajnoga xiaomi
#103735237 - telewizor
    #with open('opinions.json', 'w') as jsonfile:
    #    json.dump(opinions_object, jsonfile, indent=4)

app = Flask(__name__, template_folder="templates")

@app.route("/")
def homePage():
    return render_template('homepage/homepage.html')

@app.route("/extraction")
def extractionPage():
    return render_template('extraction/extraction.html')

@app.route("/product/<productId>")
def productPage(productId):
    ceneo_scraper = Scraper(productId)
    opinions_object = ceneo_scraper.get_all_opinions()

    return render_template('product/product.html', opinions=opinions_object)

if __name__ == '__main__':
    app.run()