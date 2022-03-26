from bs4 import BeautifulSoup

class OpinionScraper:
    def __init__(self, opinion_element):
        self.opinion_element = opinion_element

    def get_data_entry_id(self):
        return self.opinion_element['data-entry-id']

    def get_author_name(self):
        return self.opinion_element.find("span", class_="user-post__author-name").text

    def get_recommendation(self):
        recommendation = self.opinion_element.find("em", class_="recommended")
        if recommendation:
            return True
        else:
            return False

    def get_post_score_count(self):
        return self.opinion_element.find("span", class_="user-post__score-count").text

    def get_buy_confirmed(self):
        userPostPublishedElement = self.opinion_element.find("span", class_="user-post__published")
        datetimeElements = userPostPublishedElement.find_all("time")
        if len(datetimeElements) == 2:
            return True
        else:
            return False

    def get_opinion_date(self):
        userPostPublishedElement = self.opinion_element.find("span", class_="user-post__published")
        datetimeElements = userPostPublishedElement.find_all("time")
        return datetimeElements[0]['datetime']

    def get_buy_date(self):
        userPostPublishedElement = self.opinion_element.find("span", class_="user-post__published")
        datetimeElements = userPostPublishedElement.find_all("time")
        if len(datetimeElements) == 2:
            return datetimeElements[1]['datetime']
        else: 
            return None
    def get_yes_votes_count(self):
        voteYesButton = self.opinion_element.find("button", class_="vote-yes")
        return voteYesButton.find("span").text

    def get_no_votes_count(self):
        voteNoButton = self.opinion_element.find("button", class_="vote-no")
        return voteNoButton.find("span").text

    def get_opinion_text(self): 
        return self.opinion_element.find("div", class_="user-post__text").text

    def get_positives(self):
        positiveOpinions = []
        featureCols = self.opinion_element.find_all("div", class_="review-feature__col")
        for featureCol in featureCols:
            if featureCol.find("div", class_="review-feature__title--positives"):
                itemElements = featureCol.find_all("div", class_="review-feature__item")
                for itemElement in itemElements:
                    positiveOpinions.append(itemElement.text)
        return positiveOpinions

    def get_negatives(self):
        negativeOpinions = []
        featureCols = self.opinion_element.find_all("div", class_="review-feature__col")
        for featureCol in featureCols:
            if featureCol.find("div", class_="review-feature__title--negatives"):
                itemElements = featureCol.find_all("div", class_="review-feature__item")
                for itemElement in itemElements:
                    negativeOpinions.append(itemElement.text)
        return negativeOpinions