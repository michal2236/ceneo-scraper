import requests
import re
import math
from bs4 import BeautifulSoup
from opinionScraper import OpinionScraper
from opinion import Opinion

class ProductScraper:
    def __init__(self, productId):
        self.productId = productId
        self.error = False
        try:
            response = requests.get(f"https://www.ceneo.pl/{self.productId}/opinie-1")
            if response.status_code == 404:
                raise Exception('')
            self.page_dom = BeautifulSoup(response.text, 'html.parser')
            all_opinions_elements = self.page_dom.find_all("div", attrs={"class": "user-post__card"})
            opinions_menu_element = None
            review_page_tab = self.page_dom.find("li", class_="page-tab reviews active")
            if review_page_tab:
                opinions_menu_element = review_page_tab.find('span', class_="page-tab__title")
            opinions_number = 0
            if opinions_menu_element:
                findedNumbers = re.findall("[0-9]+", opinions_menu_element.text)
                if len(findedNumbers) > 0:
                    opinions_number = int(findedNumbers[0])
            
            if opinions_number > 0:
                opinion_pages = math.ceil(opinions_number / 10)
                for opinion_page in range(2, opinion_pages+1):
                    page_response = requests.get(f"https://www.ceneo.pl/{self.productId}/opinie-{opinion_page}")
                    print('DOWNLOADED PAGE: ', opinion_page)
                    dom = BeautifulSoup(page_response.text, 'html.parser')
                    all_opinions_elements.extend(dom.find_all("div", attrs={"class": "user-post__card"}))

            filtered_opinions_elements = []
            for o in all_opinions_elements:
                if o.has_attr('data-entry-id'):
                    filtered_opinions_elements.append(o)
            self.opinions_elements = filtered_opinions_elements
        except:
            self.error = True


    def get_product_name(self):
        return self.page_dom.find("h1", class_="product-top__product-info__name").text

    def get_product_opinions(self):
        opinions_object = {}
        for opinion_element in self.opinions_elements:
            opinion_scraper = OpinionScraper(opinion_element)
            opinion = Opinion(opinion_scraper.get_data_entry_id(), opinion_scraper.get_author_name(), opinion_scraper.get_recommendation(), opinion_scraper.get_post_score_count(), opinion_scraper.get_buy_confirmed(), opinion_scraper.get_opinion_date(), opinion_scraper.get_buy_date(), opinion_scraper.get_yes_votes_count(), opinion_scraper.get_no_votes_count(), opinion_scraper.get_opinion_text(), opinion_scraper.get_positives(), opinion_scraper.get_negatives())
            opinions_object.update(opinion.get_opinion_jsonable_object())
        return opinions_object

    def check_error(self):
        return self.error


    