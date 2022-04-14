import requests
from bs4 import BeautifulSoup
import time
import smtplib


class Currency:
    DOLLAR_RUB = "https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome..69i57j0i433i512j0i512l5j0i457i512j0i512l2.2758j1j1&sourceid=chrome&ie=UTF-8"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",","."))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'lxml')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",","."))
        if currency>= self.current_converted_price+self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
            self.send_mail()
        elif currency>= self.current_converted_price+self.difference:
            print("Курс сильно упал, может пора что-то делать?")
            self.send_mail()

        print("Сейчас курс: 1 доллар - "+str(currency))
        time.sleep(3)
        self.check_currency()

    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('kiorofficial2@gmail.com', 'dbyshmuunxdrsvte')

        subject = 'Currency'
        body = 'Dollar'
        message = f'Subject: {subject}\n\n{body}'

        server.sendmail(
            'kiordev@gmail.com',
            'kiorofficial2@gmail.com',
            message
        )
        server.quit()



currency = Currency()
currency.check_currency()





