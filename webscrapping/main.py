# import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


print(f'''
    -------------------
    - SHEIN X KLOTHEA -
    -------------------

''')
print('Input your link ')

# url = "https://asia.shein.com/DAZY-Figure-Letter-Graphic-Drop-Shoulder-Blouse-p-2503739-cat-1733.html?scici=WomenHomePage~~ON_SliderBanner,CN_rank,HZ_0,HI_0~~11_2~~itemPicking_00660555~~~~"

url = input('> ')

us_domain = "https://us.shein.com"
url = url.split("?")
url = url[0].split("com")
url = us_domain+url[1]

# os.environ['PATH'] += r'D:\\SeleniumDrivers'
PATH = 'D:\SeleniumDrivers\chromedriver.exe' # download from https://chromedriver.storage.googleapis.com/index.html
driver = webdriver.Chrome(PATH)

driver.get(url)
driver.implicitly_wait(10)

product_Info = driver.find_element(By.CLASS_NAME, "product-intro")
product_name = driver.find_element(By.CLASS_NAME, "product-intro__head-name").text
# product_regular_price = driver.find_element(By.CLASS_NAME, "del-price").text
product_current_price = driver.find_element(By.CLASS_NAME, "from").text
# prodcut_discount = driver.find_element(By.CLASS_NAME, "discount-label").text

print(
f'''
Product: {product_name}
Price: {product_current_price}
URL: {url}
'''
)
