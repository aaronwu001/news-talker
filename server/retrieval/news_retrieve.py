from newsdataapi import NewsDataApiClient
from dotenv import load_dotenv
import os
import json
import datetime

# Get environment variables
load_dotenv()
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

def fetch_n_pages(query=None, country=None, n=1):
    """
    Fetches up to n pages of news articles using `read_one_page`,
    combining them into a single dataset.

    Returns:

    return_result = {
        "news": list[newsObject], 
        "totalPagesFetched": int
    }
    
    where 

    newsObject = {
        article_id: str,
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
    all_news = []  # List to store all news articles
    next_page = None  # Start with the first page
    pages_fetched = 0

    while pages_fetched < n:
        result = fetch_one_page(query=query, country=country, page=next_page)
        
        # Stop if no results
        if not result or not result.get("news"):  
            print(f"No more results. Stopping after {pages_fetched} pages.")
            break

        # Append news articles from this page
        all_news.extend(result["news"])
        pages_fetched += 1

        # Get the nextPage value
        next_page = result.get("nextPage", "")
        print(f"next page: {next_page}")

        # Stop if nextPage is empty (no more pages)
        if not next_page:
            print(f"Reached last available page after {pages_fetched} pages.")
            break

    final_result = {
        "news": all_news,
        "totalPagesFetched": pages_fetched
    }
    return final_result


def fetch_one_page(query=None, country=None, page=None):
    """
    return_result = {
        news: list[newsObject], 
        nextPage: str 
    }
    
    where 

    newsObject = {
        article_id: str,
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
    
    if not NEWSDATA_API_KEY:
        print("Error: API key is missing. Please check environment.")
        return None

    api = NewsDataApiClient(apikey=NEWSDATA_API_KEY)
    response = api.news_api(q=query, country=country, page=page)

    # Ensure response is valid and contains "status"
    if not response or "status" not in response:
        print("Error: Invalid API response received.")
        return None

    # Check if API status is "success"
    if response["status"] != "success":
        print(f"API Error: {response.get('message', 'Unknown error')}")
        return None

    print(f"Query successful: q={query}, country={country}, page={page}")

    # Extract news articles into the desired format
    news = [
        {
            "article_id": article.get("article_id", ""),
            "title": article.get("title", ""),
            "link": article.get("link", ""),
            "description": article.get("description", ""),
            "pubDate": article.get("pubDate", ""),
            "pubDateTZ": article.get("pubDateTZ", ""),
            "image_url": article.get("image_url", ""),
            "source_name": article.get("source_name", "")
        }
        for article in response.get("results", []) 
    ]

    # Construct the final return_result object
    return_result = {
        "news": news,
        "nextPage": str(response.get("nextPage", ""))
    }

    return return_result


if __name__ == '__main__':
    
    QUERY = "business"
    COUNTRY= "us"
    N_PAGES = 5
    
    result = fetch_n_pages(query=QUERY, country=COUNTRY, n=N_PAGES)

    if result:
        # Create a new folder if it doesn't exist
        folder_name = "news_results"
        os.makedirs(folder_name, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder_name}/news_{timestamp}.json"

        # Save JSON file
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"News data saved to {filename}")
        print(f"Article count: {len(result)}")

    else:
        print("No data to save.")

