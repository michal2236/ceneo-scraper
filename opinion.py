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

    def get_opinion_object(self):
            opinionId = self.opinion_id
            opinion_object[opinionId] = {}
            opinion_object[opinionId]['authorName'] = self.author_name
            opinion_object[opinionId]['recommended'] = self.recommended
            opinion_object[opinionId]['postScoreCount'] = self.post_score_count
            opinion_object[opinionId]['buyConfirmed'] = self.buy_confirmed
            opinion_object[opinionId]['opinionDate'] = self.opinion_date
            opinion_object[opinionId]['buyDate'] = self.buy_date
            opinion_object[opinionId]['yesVotes'] = self.yes_votes
            opinion_object[opinionId]['noVotes'] = self.no_votes
            opinion_object[opinionId]['text'] = self.text
            opinion_object[opinionId]['positives'] = self.positives
            opinion_object[opinionId]['negatives'] = self.negatives
            return opinion_object