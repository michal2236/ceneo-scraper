class Opinion:
    def __init__(self, opinion_id, author_name, recommended, post_score_count, buy_confirmed, opinion_date, buy_date, yes_votes, no_votes, text, positives, negatives):
        self.opinion_id = opinion_id
        self.author_name = author_name
        self.recommended = recommended
        self.post_score_count = post_score_count
        self.buy_confirmed = buy_confirmed
        self.opinion_date = opinion_date
        self.buy_date = buy_date
        self.yes_votes = yes_votes
        self.no_votes = no_votes
        self.text = text
        self.positives = positives
        self.negatives = negatives

    def get_opinion_jsonable_object(self):
            opinion_object = {}
            opinion_object[self.opinion_id] = {}
            opinion_object[self.opinion_id]['authorName'] = self.author_name
            opinion_object[self.opinion_id]['recommended'] = self.recommended
            opinion_object[self.opinion_id]['postScoreCount'] = self.post_score_count
            opinion_object[self.opinion_id]['buyConfirmed'] = self.buy_confirmed
            opinion_object[self.opinion_id]['opinionDate'] = self.opinion_date
            opinion_object[self.opinion_id]['buyDate'] = self.buy_date
            opinion_object[self.opinion_id]['yesVotes'] = self.yes_votes
            opinion_object[self.opinion_id]['noVotes'] = self.no_votes
            opinion_object[self.opinion_id]['text'] = self.text
            opinion_object[self.opinion_id]['positives'] = self.positives
            opinion_object[self.opinion_id]['negatives'] = self.negatives
            return opinion_object