import requests
from dotenv import load_dotenv
import os
import json
import datetime

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

    return data_news 

""" SELECCIÓN DE NOTICIAS """

def formatJSON(jsonFile):

    data_news = "data_news.json"

    with open (data_news, "r") as news1:
        
        news = json.load(news1)
        todayNews = []
        
        for new in news:
            
            mainNew = datetime.datetime.strptime((news[0].get("publishedAt")), '%Y-%m-%dT%H:%M:%SZ').date()

            if mainNew == datetime.datetime.strptime(new.get("publishedAt"), '%Y-%m-%dT%H:%M:%SZ').date():

                newObject = {
                    "title": new.get("title"),
                    "description": new.get("description"),
                    "publishedAt": new.get("publishedAt")
                }
                todayNews.append(newObject)
            else:
                pass

        if len(todayNews) < 4:
            todayNews = news

    with open("email.txt", "w", encoding="utf-8") as fileTodayNews:
        fileTodayNews.write(str(todayNews))

""" MAIN """

def main():

    # format_data(get_news_data())
    formatJSON(format_data(get_news_data()))

