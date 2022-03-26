import requests
from bs4 import BeautifulSoup
from opinionScraper import OpinionScraper
from opinion import Opinion

class ProductScraper:
    def __init__(self, productId):
        self.productId = productId
        response = requests.get(f"https://www.ceneo.pl/{self.productId}#tab=reviews")
        self.page_dom = BeautifulSoup(response.text, 'html.parser')
        all_opinions_elements = self.page_dom.find_all("div", attrs={"class": "user-post__card"})
        filtered_opinions_elements = []
        for o in all_opinions_elements:
            if o.has_attr('data-entry-id'):
                filtered_opinions_elements.append(o)
        self.opinions_elements = filtered_opinions_elements

    def get_product_name(self):
        return self.page_dom.find("h1", class_="product-top__product-info__name").text

    def get_product_opinions(self):
        opinions_object = {}
        for opinion_element in self.opinions_elements:
            opinion_scraper = OpinionScraper(opinion_element)
            opinion = Opinion(opinion_scraper.get_data_entry_id(), opinion_scraper.get_author_name(), opinion_scraper.get_recommendation(), opinion_scraper.get_post_score_count(), opinion_scraper.get_buy_confirmed(), opinion_scraper.get_opinion_date(), opinion_scraper.get_buy_date(), opinion_scraper.get_yes_votes_count(), opinion_scraper.get_no_votes_count(), opinion_scraper.get_opinion_text(), opinion_scraper.get_positives(), opinion_scraper.get_negatives())
            opinions_object.update(opinion.get_opinion_jsonable_object())
        return opinions_object


    