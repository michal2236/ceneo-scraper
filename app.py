import json
from scraper import Scraper

product_id = '103735237'
#96092975 - hulajnoga xiaomi
#103735237 - telewizor

opinions_object = {}

ceneo_scraper = Scraper(product_id)
opinions = ceneo_scraper.get_all_opinions()

for opinion in opinions:
    opinionId = ceneo_scraper.get_data_entry_id(opinion)
    opinions_object[opinionId] = {}

    opinions_object[opinionId]['authorName'] = ceneo_scraper.get_author_name(opinion)
    opinions_object[opinionId]['recommended'] = ceneo_scraper.get_recommendation(opinion)
    opinions_object[opinionId]['postScoreCount'] = ceneo_scraper.get_post_score_count(opinion)
    opinions_object[opinionId]['buyConfirmed'] = ceneo_scraper.get_buy_confirmed(opinion)
    opinions_object[opinionId]['opinionDate'] = ceneo_scraper.get_opinion_date(opinion)
    opinions_object[opinionId]['buyDate'] = ceneo_scraper.get_buy_date(opinion)
    opinions_object[opinionId]['yesVotes'] = ceneo_scraper.get_yes_votes_count(opinion)
    opinions_object[opinionId]['noVotes'] = ceneo_scraper.get_no_votes_count(opinion)
    opinions_object[opinionId]['text'] = ceneo_scraper.get_opinion_text(opinion)
    opinions_object[opinionId]['positives'] = ceneo_scraper.get_positives(opinion)
    opinions_object[opinionId]['negatives'] = ceneo_scraper.get_negatives(opinion)

with open('opinions.json', 'w') as jsonfile:
    json.dump(opinions_object, jsonfile, indent=4)