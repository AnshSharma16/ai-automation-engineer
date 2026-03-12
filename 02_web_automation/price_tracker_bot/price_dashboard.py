import pandas as pd
import matplotlib.pyplot as plt

# load price history
df = pd.read_csv("price_history.csv")

# convert date column
df["date"] = pd.to_datetime(df["date"])

# sort values
df = df.sort_values("date")

# plot price trend
plt.figure()

plt.plot(df["date"], df["price"], marker="o")

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Product Price History")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("price_chart.png")

plt.show()