import requests
import pandas as pd
import schedule
import time

def collect_data():

    print("Running scheduled automation...")

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data)

    df.to_csv("../../outputs/scheduled_posts.csv", index=False)

    print("Data saved successfully!")

# run every 1 minute (for testing)
schedule.every(1).minutes.do(collect_data)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)