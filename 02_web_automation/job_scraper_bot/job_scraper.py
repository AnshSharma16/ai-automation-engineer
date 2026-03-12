from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://realpython.github.io/fake-jobs/")

time.sleep(3)

jobs = driver.find_elements(By.CLASS_NAME, "card-content")

job_list = []

for job in jobs:

    title = job.find_element(By.CLASS_NAME, "title").text
    company = job.find_element(By.CLASS_NAME, "company").text
    location = job.find_element(By.CLASS_NAME, "location").text

    job_list.append({
        "Title": title,
        "Company": company,
        "Location": location
    })

df = pd.DataFrame(job_list)

df.to_csv("../../outputs/jobs.csv", index=False)

print("Jobs scraped successfully")

driver.quit()