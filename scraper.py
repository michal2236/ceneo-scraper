import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, productId):
        self.productId = productId

    def get_all_opinions(self):
        response = requests.get(f"https://www.ceneo.pl/{self.productId}#tab=reviews")
        page_dom = BeautifulSoup(response.text, 'html.parser')
        opinionsElements = page_dom.find_all("div", attrs={"class": "user-post__card"})
        filteredOpinionsElements = []
        for o in opinionsElements:
            if o.has_attr('data-entry-id'):
                filteredOpinionsElements.append(o)
        return filteredOpinionsElements

    def get_data_entry_id(self, opinion):
        return opinion['data-entry-id']

    def get_author_name(self, opinion):
        return opinion.find("span", class_="user-post__author-name").text

    def get_recommendation(self, opinion):
        recommendation = opinion.find("em", class_="recommended")
        if recommendation:
            return True
        else:
            return False

    def get_post_score_count(self, opinion):
        return opinion.find("span", class_="user-post__score-count").text

    def get_buy_confirmed(self, opinion):
        userPostPublishedElement = opinion.find("span", class_="user-post__published")
        datetimeElements = userPostPublishedElement.find_all("time")
        if len(datetimeElements) == 2:
            return True
        else:
            return False

    def get_opinion_date(self, opinion):
        userPostPublishedElement = opinion.find("span", class_="user-post__published")
        datetimeElements = userPostPublishedElement.find_all("time")
        return datetimeElements[0]['datetime']

    def get_buy_date(self, opinion):
        userPostPublishedElement = opinion.find("span", class_="user-post__published")
        datetimeElements = userPostPublishedElement.find_all("time")
        if len(datetimeElements) == 2:
            return datetimeElements[1]['datetime']
        else: 
            return None
    def get_yes_votes_count(self, opinion):
        voteYesButton = opinion.find("button", class_="vote-yes")
        return voteYesButton.find("span").text

    def get_no_votes_count(self, opinion):
        voteNoButton = opinion.find("button", class_="vote-no")
        return voteNoButton.find("span").text

    def get_opinion_text(self, opinion): 
        return opinion.find("div", class_="user-post__text").text

    def get_positives(self, opinion):
        positiveOpinions = []
        featureCols = opinion.find_all("div", class_="review-feature__col")
        for featureCol in featureCols:
            if featureCol.find("div", class_="review-feature__title--positives"):
                itemElements = featureCol.find_all("div", class_="review-feature__item")
                for itemElement in itemElements:
                    positiveOpinions.append(itemElement.text)
        return positiveOpinions

    def get_negatives(self, opinion):
        negativeOpinions = []
        featureCols = opinion.find_all("div", class_="review-feature__col")
        for featureCol in featureCols:
            if featureCol.find("div", class_="review-feature__title--negatives"):
                itemElements = featureCol.find_all("div", class_="review-feature__item")
                for itemElement in itemElements:
                    negativeOpinions.append(itemElement.text)
        return negativeOpinions

        
    

#url = "https://www.ceneo.pl/96092975#tab=reviews"
#response = requests.get(url)
#page_dom = BeautifulSoup(response.text, 'html.parser')
#print(page_dom.prettify())

#opinia - user-post__author-recomendation
#user name - user-post__author-name
#treść - user-post__text
#liczba gwiazdek - user-post__score-count
#zalety - review-feature__title review-feature__title--positives
#wady - review-feature__title review-feature__title--negatives
#dla ilu przydatna - 