import requests
import datetime as dt
import vonage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alphavantage_api_key = "QY6D6NLHDV7NL0QP"
alphavantage_function = "TIME_SERIES_DAILY_ADJUSTED"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_url = 'https://www.alphavantage.co/query'
alphavantage_respond = requests.get(alphavantage_url, params={
    "function": alphavantage_function,
    "symbol": STOCK,
    "apikey": alphavantage_api_key
})
alphavantage_respond.raise_for_status()
alphavantage_data = alphavantage_respond.json()["Time Series (Daily)"]
yesterday = dt.datetime.today() - dt.timedelta(days=1)
while True:
    try:
        yesterday_data = alphavantage_data[str(yesterday).split(" ")[0]]
        break
    except KeyError:
        yesterday -= dt.timedelta(days=1)
the_day_before_yesterday = yesterday - dt.timedelta(days=1)
while True:
    try:
        the_day_before_yesterday_data = alphavantage_data[str(the_day_before_yesterday).split(" ")[0]]
        break
    except KeyError:
        the_day_before_yesterday -= dt.timedelta(days=1)
percentage = ((float(yesterday_data["4. close"]) - float(the_day_before_yesterday_data["4. close"]))
              / float(yesterday_data["4. close"])) * 100
percentage = round(percentage, 2)

if abs(percentage) >= 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    newsapi_api_key = "8f42d144e3064b59bbcf5e00d5135adf"
    newsapi_url = "https://newsapi.org/v2/everything"
    newsapi_respond = requests.get(newsapi_url, params={
        "apiKey": newsapi_api_key,
        "q": STOCK,
        "from": the_day_before_yesterday,
        "to": yesterday,
        "sortBy": "popularity"
    })
    newsapi_respond.raise_for_status()
    first_three_articles = newsapi_respond.json()["articles"][:3]
    print(first_three_articles)

    ## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
vonage_api_key = "12447eeb"
vonage_api_secret = "sFJFalnpyN9qo4yA"
client = vonage.Client(key=vonage_api_key, secret=vonage_api_secret)
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "stocks console",
        "to": "",
        "text": "hello",
    }
)
print(responseData)
if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
