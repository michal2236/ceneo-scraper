import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/96092975#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, 'html.parser')
print(page_dom.prettify())

#opinia - user-post__author-recomendation
#user name - user-post__author-name
#treść - user-post__text
#liczba gwiazdek - user-post__score-count
#zalety - review-feature__title review-feature__title--positives
#wady - review-feature__title review-feature__title--negatives
#dla ilu przydatna - 