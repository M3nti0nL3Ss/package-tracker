from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import sys

URL = "https://www.1tracking.net/en/detail?nums=" + str(sys.argv[1])
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.get(URL)
sleep(10)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

find_date = soup.select("#app > div.view > div > div.search-result.result-detail-content > div.track-detail > div.track-center > div > div > div.track-result-content > div > div.track-pandect > ul > li.result-li-three > div > div > div.text-gray")[0].text

print(find_date)
