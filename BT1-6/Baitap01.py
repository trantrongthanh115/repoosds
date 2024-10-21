from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao webdriver
driver = webdriver.Chrome()

# Mo trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)

# Doi khoang chung 2 giay
time.sleep(2)

# Lay tat ca cac the <a>
tags = driver.find_elements(By.TAG_NAME, "a");

# Tao ra danh sach cac lien ket
links = [tag.get_attribute("href") for tag in tags]

# Xuat thong tin
for link in links:
    print(link)

# Dong webdriver
driver.quit()