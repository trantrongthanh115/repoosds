from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao webdriver
driver = webdriver.Chrome()

# Mo trang
url = "http://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
driver.get(url)

# Doi mot chut de tai trang
time.sleep(2)

# Lay ra tat cac ca the ul
ul_tags = driver.find_elements(By.TAG_NAME, "ul")

# Chon the ul thu 21
ul_painters = ul_tags[20] # list start with index=0

# Lay ra tat ca the <li> thuoc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

# Tao danh sach cac url
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]
# In ra url
for link in links:
    print(link)

for title in titles:
    print(title)

driver.quit()
