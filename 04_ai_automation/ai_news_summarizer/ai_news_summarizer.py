import requests
import pandas as pd

NEWS_API = "https://newsapi.org/v2/top-headlines"
API_KEY = "cf66cd88e32643128e32fd667156d38b"

params = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(NEWS_API, params=params)

data = response.json()

articles = data["articles"]

news_list = []

for article in articles:

    news_list.append({
        "title": article["title"],
        "summary": article["description"]
    })

df = pd.DataFrame(news_list)

df.to_csv("ai_news_report.csv", index=False)

print("AI news report generated")