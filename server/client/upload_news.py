import json
import os
import sys
import datetime
sys.path.append('./../pc_assistant')
sys.path.append('./../retrieval')
from assistant import get_or_create_assistant, upload_file
from news_retrieve import fetch_n_pages

def retrieve_and_upsert_news(assistant_name: str, query: str, country: str =None, n_pages: int =1):
    fetch_result = fetch_n_pages(query=None, country=country, n=n_pages)
    assistant = get_or_create_assistant(assistant_name)

    # create new folder for this news retrieval
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dir_name = f"news_retrieval_{timestamp}"
    os.makedirs(dir_name, exist_ok=True)

    news_list = fetch_result.get("news", [])
    for news in news_list:
        attributes = ["article_id", "title", "link", "pubDate", "pubDateTZ", "image_url", "source_name"] # everything except description
        metadata = {attr: news.get(attr, "") for attr in attributes}

        # filename set to article id
        filename = f"{dir_name}/{news.get("article_id")}.json"

        # Save JSON file
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(news, file, indent=4)

        upload_file(assistant, file_path=filename, metadata=metadata)
    

if __name__ == '__main__':
    assistant_name = "business-us-dev"
    query = "business"
    country = "us"
    n_pages = 5
    retrieve_and_upsert_news(assistant_name, query, country, n_pages)