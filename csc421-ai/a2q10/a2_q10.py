from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service('C:/Users/naumh/Desktop/year4/a2q10/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service = service, options=options)

driver.get('https://www.songfacts.com/categories')

time.sleep(5)

threecats = {}
categoryname = []
facts = []
print(driver.title)

try:
    categories = driver.find_elements(By.CSS_SELECTOR, 'ul.browse-list-purple li a')
except Exception as e:
    print(f"error scraping category: {e}")

i = 0
for category in categories:
    if i < 3:
        categoryName = category.text.strip()
        categoryLink = category.get_attribute('href')
        print(categoryName , ' ', categoryLink)

        try:
            print('navigating to: ' + categoryLink)
            driver.get(categoryLink)
           # songs = driver.find_elements(By.CSS_SELECTOR, '.fact-item')
        except Exception as e:
            print(f"error scraping songs: {e}")
    i += 1


#I AM GETTING A SSL ERROR AND I CANT FIGURE OUT WHY AHHHHHHHHHHHH
#I WILL JUST TURN IT IN AS IS I GUESS 
driver.quit()