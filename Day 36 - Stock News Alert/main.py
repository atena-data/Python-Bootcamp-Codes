import requests
import datetime as dt
from twilio.rest import Client

YESTERDAY = (dt.datetime.today() - dt.timedelta(1)).date()
DAY_BEF_YESTERDAY = (dt.datetime.today() - dt.timedelta(2)).date()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "KX6R2WDEZRUGTZ6N"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "a5a3fe06384b49bebd60ec6204add7a9"
NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# variables to use Twilio API for messaging
account_sid = "ACc93427e5a223e5eb0d271674eed00c2a"
auth_token = "a937fabea54d1dab045920eb720e02ec"

# Check STOCK price increase/decreases between yesterday and the day before yesterday.
stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_response.raise_for_status()
daily_stock = stock_response.json()["Time Series (Daily)"]

# Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices.
yesterday_price = float(daily_stock[str(YESTERDAY)]["4. close"])
day_bef_yesterday_price = float(daily_stock[str(DAY_BEF_YESTERDAY)]["4. close"])

price_change = (yesterday_price - day_bef_yesterday_price) * 100 / yesterday_price

# symbols for +/- price change
if price_change >= 5:
    sign = f"🔺 {round(price_change)}"
elif price_change <= -5:
    sign = f"🔻 {round(price_change)}"

# Check the news for the relevant articles
if abs(price_change) >= 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news = news_response.json()["articles"]

    # fetch the first 3 articles for the COMPANY_NAME.
    for article in news[:3]:
        news_title = article["title"]
        desc = article["description"]
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{STOCK} {sign}%\nHeadline: {news_title}\nBrief: {desc}.",
                from_="+14439032421",
                to="+15558675310"
            )
        print(message.status)
