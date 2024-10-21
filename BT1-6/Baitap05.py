from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import regex as re

# Tao dataframe rong
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Khoi tao webdriver
driver = webdriver.Chrome()

# Mo trang
url = "http://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

# Doi 2 giay
time.sleep(2)

# Lay ten hoa si
try:
    name = driver.find_element(By.TAG_NAME, "h1").text
except:
    name = ""

# Lay ngay sinh
try:
    brith_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    brith = brith_element.text
    brith = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', brith)[0]
except:
    brith = ""

# Lay ngay mat
try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""


try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ""

# Tao dictionary thong tin cua hoa si
painter_DF = {'name': name, 'brith': brith, 'death': death, 'nationality': nationality}

# Chuyen thanh DataFrame
painter_DF = pd.DataFrame([painter_DF])

# Them thong tin vao DF chinh
d = pd.concat([d, painter_DF], ignore_index=True)

# In ra DF
print(d)

 # Dong webdriver
driver.quit()

