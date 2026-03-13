import requests
import pandas as pd

URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "cf66cd88e32643128e32fd667156d38b"

params = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(URL, params=params)

data = response.json()

articles = data["articles"]

news_list = []

for article in articles:

    news_list.append({
        "title": article["title"],
        "source": article["source"]["name"],
        "published": article["publishedAt"]
    })

df = pd.DataFrame(news_list)

df.to_csv("news_data.csv", index=False)

print("News data pipeline executed successfully")