from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

MY_EMAIL = "codetestpython@gmail.com"
MY_PASSWORD = "abcd1234()"
URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324."
                  "150 Safari/537.36",
    "Accept-Language": "en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5,fa;q=0.4"
}

response = requests.get(URL, headers=headers)
website = response.text

# scrape the website for the item price
soup = BeautifulSoup(website, "lxml")
price_tag = soup.find(id="priceblock_ourprice").getText()
price = float(price_tag.strip()[1:])

target_price = 100

# compare target and actual price, if it's reached the target send an alert email.
if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Amazon Price Alert! \n\nThe product price is now {price}, below your target price. "
                                f"Buy it now!")
