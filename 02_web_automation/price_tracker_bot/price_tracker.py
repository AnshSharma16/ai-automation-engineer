from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Target price you want to buy at
TARGET_PRICE = 40

# Product URL
URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def check_price():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(URL)

    wait = WebDriverWait(driver,10)

    try:

        # get product title
        title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".product_main h1"))
        ).text

        # get product price
        price_text = driver.find_element(By.CLASS_NAME,"price_color").text

        # convert price to float
        current_price = float(price_text.replace("£",""))

        print("Product:", title)
        print("Current Price:", current_price)

        # compare price
        if current_price < TARGET_PRICE:
            print("Price dropped! Buy now!")
        else:
            print("Price still high.")

    except Exception as e:

        print("Error extracting product information:", e)

    finally:

        driver.quit()


if __name__ == "__main__":
    check_price()