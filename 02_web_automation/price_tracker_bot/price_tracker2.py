from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import schedule
import smtplib
import time
from datetime import datetime
import os


# -------------------------
# CONFIG
# -------------------------

URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

TARGET_PRICE = 40

EMAIL = "anshsharmacs22@gmail.com"
PASSWORD = "Ansh@Google123"
TO_EMAIL = "asindoraptor@gmail.com"

CSV_FILE = "price_history.csv"


# -------------------------
# SEND EMAIL ALERT
# -------------------------

def send_email(product, price):

    subject = "Price Drop Alert!"

    body = f"{product} is now £{price}\nCheck it here:\n{URL}"

    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.sendmail(EMAIL, TO_EMAIL, message)

    server.quit()

    print("Email alert sent!")


# -------------------------
# SAVE PRICE HISTORY
# -------------------------

def save_price(product, price):

    data = {
        "date": datetime.now(),
        "product": product,
        "price": price
    }

    df = pd.DataFrame([data])

    if os.path.exists(CSV_FILE):

        df.to_csv(CSV_FILE, mode="a", header=False, index=False)

    else:

        df.to_csv(CSV_FILE, index=False)


# -------------------------
# SCRAPE PRICE
# -------------------------

def check_price():

    print("Checking price...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    try:

        title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product_main h1"))
        ).text

        price_text = driver.find_element(By.CLASS_NAME, "price_color").text

        price = float(price_text.replace("£", ""))

        print("Product:", title)
        print("Current Price:", price)

        save_price(title, price)

        if price < TARGET_PRICE:

            print("Price dropped!")

            send_email(title, price)

        else:

            print("Price still high.")

    except Exception as e:

        print("Error:", e)

    finally:

        driver.quit()


# -------------------------
# SCHEDULER
# -------------------------

schedule.every(1).hours.do(check_price)

print("Price tracker started...")

check_price()

while True:

    schedule.run_pending()

    time.sleep(60)