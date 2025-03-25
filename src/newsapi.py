import requests
from dotenv import load_dotenv
import os
import json

""" AUTENTIFICACIÓN DE NEWSAPI """

def get_news_data():

    load_dotenv(".env")
    APIKEY = os.getenv("APIKEY_NEWS")

    category = "politics" #He probado con business y technology. Economy no funciona, no sé si se refiere también a business
    base_url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey="
    api_key = APIKEY

    request = requests.get(f"{base_url}{api_key}")

    news_data = request.json()

    return news_data

""" RECOPILACIÓN DE NOTICIAS """

def format_data(news_data):

    news = []
    data_news = "data_news.json"

    for new in news_data["articles"]:
        
        report = {
            "title": new.get("title"),
            "description": new.get("description"),
            "publishedAt": new.get("publishedAt")
        }

        news.append(report)

    with open(data_news, "w") as data_news:
        json.dump(news, data_news)

""" MAIN """

def main():

    format_data(get_news_data())

main()