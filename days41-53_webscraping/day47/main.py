import requests
from bs4 import BeautifulSoup
import sys

sys.path.append("/home/muhammad/python/100DaysChallenge/days32-40_api/day39_telegram/")
from notification_manager import NotificationManager

url = "https://www.amazon.com/dp/B087H9ZVKD/ref=sbl_dpx_kitchen-electric-cookware_B0B7P646FD_0?th=1"
response = requests.get(url,
                        headers={
                            "upgrade-insecure-requests": "1",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                          "Chrome/109.0.0.0 Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                                      "image/apng,*/*;q=0.8,"
                                      "application/signed-exchange;v=b3;q=0.9"
                        })
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
price = soup.select_one(".a-price.priceToPay .a-offscreen").string[1:]
if float(price) < 250.00:
    notificationmanager = NotificationManager()
    notificationmanager.send_telegram_message(f"Amazon Price Alert!\n\ngo purshuse it right "
                                              f"nowwww at {price}\n{url}")
