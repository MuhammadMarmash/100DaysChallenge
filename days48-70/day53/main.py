import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -----------------------BeautifulSoup------------------------
site = requests.get(
    "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBo"
    "unds%22%3A%7B%22north%22%3A37.8851146460015%2C%22east%22%3A-122.2736844194336%2C%22south%22%3A37.6653058"
    "8063085%2C%22west%22%3A-122.5929745805664%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filte"
    "rState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3"
    "A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%"
    "2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%"
    "22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22"
    "isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D"
    "%5D%7D",
    headers={
        "authority": "www.zillow.com",
        "method": "GET",
        "path": '/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B'
                '%22north%22%3A37.8851146460015%2C%22east%22%3A-122.30338183764648%2C%22south%22%3A37.6653058806'
                '3085%2C%22west%22%3A-122.56327716235351%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%'
                '7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterSta'
                'te%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%2'
                '2%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3'
                'Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%2'
                '2%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%2'
                '2%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D',
        "scheme": 'https',
        "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.'
                  '8,application/signed-exchange;v=b3;q=0.9',
        "accept-encoding": 'gzip, deflate, br',
        "accept-language": 'en,en-US;q=0.9,ar;q=0.8,he-IL;q=0.7,he;q=0.6,hy;q=0.5',
        "cache-control": 'max-age=0',
        "cookie": 'x-amz-continuous-deployment-state'
                  '=AYABeFTTqNp3G9yt2i3WXMBI8ToAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzl'
                  'QQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADBf9ZWsE5Pn%2FBSJc9QAwJ0jHwbaQlp91CTdz3Vyldsny7bdcKlzTiwLG'
                  'YtARKVzpwb6xE9YE49DPeT4rdAo9AgAAAAAMAAQAAAAAAAAAAAAAAAAAABgtdQwvw2+kO6wFr4krrk3%2F%2F%2F%2F%2FAAAAA'
                  'QAAAAAAAAAAAAAAAQAAAAz2kUc8UCdZY8rOIXhaXK9yO9DkjRUQ+nvBKAHyjRUQ+nvBKAHy; JSESSIONID=58DF56ECA50DC68E'
                  'F18F49992BED68B9; zguid=24|%24c227daf6-69d6-43b6-ab26-ce1a5bbc3c8b; zgsession=1|937a5269-138c-4feb-8'
                  'd5a-8a74066a0ff2; zjs_user_id=null; zg_anonymous_id=%2267abce77-bb09-497a-bdee-11448679cf5f%22; _ga='
                  'GA1.2.1580242387.1677054505; _gid=GA1.2.18421356.1677054505; zjs_anonymous_id=%22c227daf6-69d6-43b6-'
                  'ab26-ce1a5bbc3c8b%22; pxcts=e0a25f08-b28a-11ed-921f-617554706f67; _pxvid=e0a246db-b28a-11ed-921f-617'
                  '554706f67; x-amz-continuous-deployment-state=AYABeFTTqNp3G9yt2i3WXMBI8ToAPgACAAFEAB1kM2Jsa2Q0azB3azl'
                  'vai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADBf9ZWsE5Pn%2FB'
                  'SJc9QAwJ0jHwbaQlp91CTdz3Vyldsny7bdcKlzTiwLGYtARKVzpwb6xE9YE49DPeT4rdAo9AgAAAAAMAAQAAAAAAAAAAAAAAAAAA'
                  'BgtdQwvw2+kO6wFr4krrk3%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAz2kUc8UCdZY8rOIXhaXK9yO9DkjRUQ+nvBKAH'
                  'y; _gcl_au=1.1.1588673073.1677054528; DoubleClickSession=true; __pdst=cb10a1bc186545f68f34d935e72308'
                  '4c; _pin_unauth=dWlkPU9ERTVOVEZqWlRBdFltUm1NaTAwTXpsaUxXRmxZakV0WldVeU1UQmtOVEk0WVRBMA; _clck=71zaz0'
                  '|1|f9c|0; G_ENABLED_IDPS=google; search=6|1679646987159%7Crect%3D37.844458635052476%252C-122.2736844'
                  '194336%252C37.706060503063554%252C-122.5929745805664%26rid%3D20330%26disp%3Dmap%26mdm%3Dauto%26p%3D1'
                  '%26z%3D0%26beds%3D1-%26price%3D0-872627%26mp%3D0-3000%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%'
                  '26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3'
                  'D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0'
                  '%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvail'
                  'abilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0920330%09%09%09%09%09%09; FSs'
                  'ampler=689357475; AWSALB=jzjU0VBIVXo+BSC1v5xqv+WQx7eZ6UAApOe9NgiHWzh9pU6vnxe34sKYFOUzyAlsGRVydzk71h'
                  'zCYJ0mVALKuhZ8cZyteiE7Y7IgKmOycf0NJkflKoMl/uJobzox; AWSALBCORS=jzjU0VBIVXo+BSC1v5xqv+WQx7eZ6UAApOe9'
                  'NgiHWzh9pU6vnxe34sKYFOUzyAlsGRVydzk71hzCYJ0mVALKuhZ8cZyteiE7Y7IgKmOycf0NJkflKoMl/uJobzox; _uetsid=e'
                  'e4078d0b28a11edbebcbbeadca8bc5d; _uetvid=ee40cf70b28a11edb7bff924e1b021f2; _clsk=xxe256|16770550009'
                  '80|9|0|l.clarity.ms/collect; _px3=671d71042cd32b7c9f8dea331ea6ab88f9dc3ce1cbe1e5b699ab9c53ef4b3a62:'
                  'FGZi/KDUUJy1j+WYQ/o/8Kg+WwZLVXqBCT1jqqkD2uxllf/B0y/ylI+hKpMWi8z+ztoAQqmxXkjnBU+wnisKVg==:1000:RT5wS'
                  'xwfdnQt22fVjyrrnIZc3jCYHop38PNZpgdMiXu6NpHLaX+2b4jquZcSeQyEMIrEtKA5O+MY8xymWXvonzpFrmnKzgYtx4vT/NON'
                  'EL7YvFsquZktwJI1RIPscHBhS5Nw11taQ0OcA0X+se2mY8v3eOD6RUVcz7YT8qeHyDdoVE4tLScw7t1y0ygDFOufzs+15VNTAap'
                  '4WmWqJhugiw==',
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": 'document',
        "sec-fetch-mode": 'navigate',
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safar"
                      "i/537.36"
    })
soup = BeautifulSoup(site.text, "lxml")
links = []
prices = []
addresses = []
elements1 = soup.select(".cTLZKy")
for element1 in elements1[:-1]:
    link = element1.get("href")
    if "https://www.zillow.com" not in str(link):
        link = "https://www.zillow.com" + str(link)
    links.append(link)
    addresses.append(element1.string)

elements2 = soup.select(".gugdBn span")
for element2 in elements2:
    price = element2.string
    if "+" in price:
        price = price.split("+")[0]
    else:
        price = price.split("/")[0]
    prices.append(price)


# ---------------------------selenium------------------------


chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://forms.gle/PZBfBPGNHzty7FUG9")

for i in range(len(prices)):
    time.sleep(2)
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.whsOnd.zHQkBf')))
    elements[0].send_keys(addresses[i])
    elements[1].send_keys(prices[i])
    elements[2].send_keys(links[i])
    driver.find_element(By.CSS_SELECTOR, '.NPEfkd.RveJvd.snByac')

    another = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'a')))
    another.click()
