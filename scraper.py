import requests
from bs4 import BeautifulSoup


product_code = input("Podaj kod produktu: ")
url=f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons= requests.get(url)
print(respons.status_code)
if respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    print(type(opinions))
    if len(opinions) > 0:
        opinions_all = []
        for opinion in opinions:
            single_opinion = {
                "opinion_id": page_dom.select("data-entry-id"),
                "author": page_dom.select("user-post__author-name"),
                "recommendation:": page_dom.select("user-post__author-recomendation"),
                "stars": page_dom.select("user-post__score-count"),
                "purchased": page_dom.select("review-pz"),
                "opinion_date":page_dom.select("div.js_product-review") ,
                "purchse_date": page_dom.select("div.js_product-review"), 
                "usefull_count": page_dom.select("votes-yes"),
                "content":page_dom.select("review-box-text js_review-text"),
                "pros":page_dom.select("review-feature__title review-feature__title--positives"),
                "cons":page_dom.select("review-feature__title review-feature__title--negatives"),
            }
    else:
        print("Nie ma opinii")