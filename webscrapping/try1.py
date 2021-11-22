import time
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += r"D:/SeleniumDrivers"
# PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome()
#
# url = "https://asia.shein.com/DAZY-Figure-Letter-Graphic-Drop-Shoulder-Blouse-p-2503739-cat-1733.html?scici=WomenHomePage~~ON_SliderBanner,CN_rank,HZ_0,HI_0~~11_2~~itemPicking_00660555~~~~"
# us_domain = "https://us.shein.com"
# url = url.split("?")
# url = url[0].split("com")
# url = us_domain+url[1]
#
# driver.get(url)
# product = driver.find_element_by_class_name("product-intro")
# time.sleep(5)
# driver.quit()
#
# # html_text = requests.get(url, stream=True).text
# html_text = driver.page_source
# # print(html_text)
#
# soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify())


# jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
# for job in jobs:
#     published_date = job.find('span', class_="sim-posted").span.text
#     if 'few' in published_date:
#         company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
#         skills = job.find('span', class_="srp-skills").text.replace(' ', '')
#         # print(skills)
#         # print(company_name)
#         # print(published_date)
#         print(f'''
#             Company Name: {company_name}
#             Required Skills: {skills}
#             Time: {published_date}
#             ''')
#         print(' ___ ')
#
#
#
#
#
