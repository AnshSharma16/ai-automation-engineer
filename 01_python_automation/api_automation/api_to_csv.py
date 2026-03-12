import requests
import pandas as pd

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# request data
response = requests.get(url)

# convert JSON → python object
data = response.json()

# convert to dataframe
df = pd.DataFrame(data)

# save CSV
df.to_csv("../../outputs/posts_data.csv", index=False)
print("Data downloaded and saved as CSV.")