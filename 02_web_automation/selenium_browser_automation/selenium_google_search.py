from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# automatically install correct chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")

time.sleep(2)

search_box = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME,"q"))
)

search_box.send_keys("AI automation engineer")

search_box.send_keys(Keys.RETURN)

time.sleep(5)

print("Search executed successfully")

driver.quit()