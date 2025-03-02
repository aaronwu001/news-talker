from newsdataapi import NewsDataApiClient
from dotenv import load_dotenv
import os
import json

# Get environment variables
load_dotenv()
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey=NEWSDATA_API_KEY)

# You can pass empty or with request parameters {ex. (country = "us")}
# response = api.news_api(q =None , country =None, page=None)
response = api.news_api(q=None, country="us", page=None)

with open('new_york_us-2', "w", encoding="utf-8") as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

print(response)