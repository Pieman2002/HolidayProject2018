from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time
from variables import *
import html2text

count = 0
url = 'https://hmccree.github.io/HolidayProject2018/'
interval = int(input('interval [seconds]: '))
if(interval <= 10):
    print('too low, defaulting to 15')
    interval = 15

def send_message():
    client = Client(account_sid, auth_token)
    client.messages.create(body='Page has changed',to=my_phone_number,from_=twilio_phone_number)

def scrape_site():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = str(soup)
    web_text = html2text.html2text(text)
    return(web_text)

while True:
    text_original = scrape_site()
    time.sleep(interval)
    text_updated = scrape_site()
    count += 1
    print('check ' + str(count))
    if(text_original != text_updated):
        print('changed')
        send_message()
        continue