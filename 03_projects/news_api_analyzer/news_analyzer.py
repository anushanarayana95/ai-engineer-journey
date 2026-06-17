import requests

API_KEY = "8b390caa5b8341729ba9e2b87e82b1c9"

url = (
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&apiKey={API_KEY}"
)

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()
print(data.keys())
# print(data["articles"][0])
print(data["articles"][0]["title"])

first_article = data["articles"][0]

print("Title:")
print(first_article["title"])

print("\nSource:")
print(first_article["source"]["name"])

print("\nPublished:")
print(first_article["publishedAt"])

articles = data["articles"]

for article in articles[:10]:

    print("\nTitle:")
    print(article["title"])

    print("Source:")
    print(article["source"]["name"])

    print("Published:")
    print(article["publishedAt"])

    print("-" * 50)

    import pandas as pd

news_data = []

for article in articles:

    news_data.append({
        "title": article["title"],
        "source": article["source"]["name"],
        "published": article["publishedAt"]
    })

df = pd.DataFrame(news_data)

print(df.head())
print(df.shape)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nNews Sources:")
print(df["source"].value_counts())

print("\nTotal Sources:")
print(df["source"].nunique())
df.to_csv("news_report.csv", index=False)

print("CSV Export Successful")
