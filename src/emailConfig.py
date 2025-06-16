from newsapi import *
import yagmail
from dotenv import load_dotenv
import os

def sendEmail():

    load_dotenv(".env")
    PASSWORD = os.getenv("PASSWORD_EMAIL")

    email = "ropeda98publi@gmail.com"

    yag = yagmail.SMTP(user=email, password=PASSWORD)
    content = ["./email.txt"]

    yag.send("davidrally09@gmail.com", "GUIONES", content)

def cleanAll():

    JSONfile = "./data_news.json"
    TXTfile = "./email.txt"

    os.remove(JSONfile)
    os.remove(TXTfile)

