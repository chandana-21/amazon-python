import requests
from bs4 import BeautifulSoup as bs
import smtplib
import time

URL = 'https://www.amazon.in/dp/1791392792/?coliid=I1Q6Q1GN90M81Q&colid=34HQJ9T6JADS3&psc=1&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = bs(page.content, 'html.parser')

    price = soup.find("span", {'class':'offer-price'}).get_text()
    int_price = int(price[1:2]+price[3:5])*10
    print(int_price)
    if int_price > 800:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() 
    server.starttls()
    server.ehlo()

    server.login('mailsofck@gmail.com','pqxmiciqzvdaaxjc')

    subject = 'Price fell down for Verity!!!!!'
    body = 'Check the link please and order quick: https://www.amazon.in/dp/1791392792/?coliid=I1Q6Q1GN90M81Q&colid=34HQJ9T6JADS3&psc=1&ref_=lv_ov_lig_dp_it'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mailsofck@gmail.com', #from
        'mailsofck@gmail.com', #to
        msg
    )

    server.sendmail

    print("Email has been sent!")

    server.quit()

while True:
    check_price()
    time.sleep(60*60)
