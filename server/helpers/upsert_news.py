import json
import sys
sys.path.append('./../db')
from pinecone_store import pinecone_store

def upsert_from_json(retrieved_news):
    """
    Return the number of articles upserted.
    Expect retrieved new in JSON format

    retrieved_news = {
        news: list[newsObject], 
    }
    
    where 

    newsObject = {
        article_id: str
        title: str, 
        link: str, 
        description:str, 
        pubDate: str, 
        pubDateTZ; str, 
        image_url: str, 
        source_name: str
    }

    Null values are represented by empty strings. 
    """

    data = []
    for article in retrieved_news:
        
        article_id = article.get("article_id") or ""
        title = article.get("title") or ""
        description = article.get("description") or ""

        if article_id == "": 
            continue
        
        if title:
            data.append({"id": f"{article_id}-title", "text": title})

        if description:
            data.append({"id": f"{article_id}-description", "text": description})

    if data:
        pinecone_store(data)

    n_upserted = len(data) 
    return n_upserted 
    

if __name__ == '__main__':
    file_path = './../retrieval/dev_testing/news_results/news_2025-03-01_18-29-56.json'

    with open(file_path, "r", encoding="utf-8") as f:
        retrieved_news = json.load(f)  

    # for article in retrieved_news:
    #     print(f"len_title: {len(article.get("title") or "")}, len_description: {len(article.get("description") or "")}")

    n_input = len(retrieved_news)
    n_upserted = upsert_from_json(retrieved_news)
    print(f"Upsert Result: {n_input} / {n_upserted} upserted")