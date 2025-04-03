from pinecone import Pinecone
from dotenv import load_dotenv
import os
import time

# Get environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE")
PINECONE_EMBEDDING_MODEL = os.getenv("PINECONE_EMBEDDING_MODEL")

# client function
def pinecone_store(data):
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index_name = PINECONE_INDEX_NAME
    embedding_model = PINECONE_EMBEDDING_MODEL
    namespace = PINECONE_NAMESPACE
    embeddings = create_vector_embeddings(pc, data, embedding_model)
    upsert(pc, index_name, namespace, data, embeddings)

# helper function
def create_vector_embeddings(pc, data, embedding_model):
    embeddings = pc.inference.embed(
        model=embedding_model,
        inputs=[d['text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )
    print("=== first embedding ===")
    print(embeddings[0])
    return embeddings

# helper function
def upsert(pc, index_name, namespace, data, embeddings):
    # Wait for the index to be ready
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

    index = pc.Index(index_name)

    vectors = []
    for d, e in zip(data, embeddings):
        vectors.append({
            "id": d['id'],
            "values": e['values'],
            "metadata": {'text': d['text']}
        })

    index.upsert(
        vectors=vectors,
        namespace=namespace
    )

# sample usage
if __name__ == '__main__':
    # data = [
    #     {"id": "store_sample_vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    #     {"id": "store_sample_vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    #     {"id": "store_sample_vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    #     {"id": "store_sample_vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    #     {"id": "store_sample_vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    #     {"id": "store_sample_vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
    # ]

    news_data = [
        {
            "article_id": "d0c7ee4cbd652c6f54717a4b8cfdb728",
            "title": "KLP Kapitalforvaltning AS Makes New $404.55 Million Investment in Alphabet Inc. (NASDAQ:GOOGL)",
            "link": "https://www.americanbankingnews.com/2025/04/02/klp-kapitalforvaltning-as-makes-new-404-55-million-investment-in-alphabet-inc-nasdaqgoogl.html",
            "description": "KLP Kapitalforvaltning AS purchased a new stake in Alphabet Inc. (NASDAQ:GOOGL – Free Report) during the fourth quarter, according to the company in its most recent disclosure with the SEC. The firm purchased 2,137,060 shares of the information services provider’s stock, valued at approximately $404,545,000. Alphabet makes up approximately 1.9% of KLP Kapitalforvaltning AS’s investment [...]",
            "pubDate": "2025-04-02 09:25:04",
            "pubDateTZ": "UTC",
            "image_url": "https://www.marketbeat.com/logos/google-inc-logo-1200x675.png",
            "source_name": "Americanbankingnews"
        },
        {
            "article_id": "793a82dfb1f6c0aa24524169c76ed6db",
            "title": "Vanguard Group Inc. Decreases Stock Holdings in SkyWest, Inc. (NASDAQ:SKYW)",
            "link": "https://www.americanbankingnews.com/2025/04/02/vanguard-group-inc-decreases-stock-holdings-in-skywest-inc-nasdaqskyw.html",
            "description": "Vanguard Group Inc. lessened its stake in shares of SkyWest, Inc. (NASDAQ:SKYW – Free Report) by 0.0% during the fourth quarter, according to the company in its most recent 13F filing with the Securities & Exchange Commission. The fund owned 4,818,085 shares of the transportation company’s stock after selling 1,608 shares during the quarter. Vanguard [...]",
            "pubDate": "2025-04-02 09:25:04",
            "pubDateTZ": "UTC",
            "image_url": "https://www.marketbeat.com/logos/skywest-inc-logo-1200x675.png?v=20221206124135",
            "source_name": "Americanbankingnews"
        },
        {
            "article_id": "a9b2f34bbd046040807a9bcaa5f50349",
            "title": "Sykon Capital LLC Sells 136 Shares of Alphabet Inc. (NASDAQ:GOOGL)",
            "link": "https://www.americanbankingnews.com/2025/04/02/sykon-capital-llc-sells-136-shares-of-alphabet-inc-nasdaqgoogl.html",
            "description": "Sykon Capital LLC reduced its stake in Alphabet Inc. (NASDAQ:GOOGL – Free Report) by 10.8% during the 4th quarter, according to the company in its most recent 13F filing with the Securities and Exchange Commission. The firm owned 1,129 shares of the information services provider’s stock after selling 136 shares during the period. Sykon Capital [...]",
            "pubDate": "2025-04-02 09:25:04",
            "pubDateTZ": "UTC",
            "image_url": "https://www.marketbeat.com/logos/google-inc-logo-1200x675.png",
            "source_name": "Americanbankingnews"
        },        {
            "article_id": "df20e6f90f58457f4f556b06b9d3ac40",
            "title": "Texas and Florida Homes Are Selling Below Asking Price",
            "link": "https://www.newsweek.com/texas-florida-homes-selling-below-asking-price-2053995",
            "description": "The top five U.S. metros with the highest shares of homes fetching less than the asking price are concentrated in the pandemic boom states of Florida and Texas.",
            "pubDate": "2025-04-02 09:25:00",
            "pubDateTZ": "UTC",
            "image_url": "https://d.newsweek.com/en/full/2619125/homes-sale-texas.jpg",
            "source_name": "Newsweek"
        },
        {
            "article_id": "94d797d87efafe2deb1e1e20095c4e6f",
            "title": "Alphabet Inc. (NASDAQ:GOOGL) Stake Increased by Fi3 FINANCIAL ADVISORS LLC",
            "link": "https://www.defenseworld.net/2025/04/02/alphabet-inc-nasdaqgoogl-stake-increased-by-fi3-financial-advisors-llc.html",
            "description": "Fi3 FINANCIAL ADVISORS LLC grew its stake in shares of Alphabet Inc. (NASDAQ:GOOGL – Free Report) by 2.6% in the 4th quarter, according to the company in its most recent 13F filing with the Securities and Exchange Commission (SEC). The institutional investor owned 9,648 shares of the information services provider’s stock after acquiring an additional [...]",
            "pubDate": "2025-04-02 09:24:45",
            "pubDateTZ": "UTC",
            "image_url": "https://www.marketbeat.com/logos/google-inc-logo-1200x675.png",
            "source_name": "Defenseworld Net"
        }
    ]

    data = []
    for article in news_data:
        article_object = {
            "id": article.get("article_id", article.get("link", "")),
            "text": (article.get("title") or "") + "\n" + (article.get("description") or "")
        }
        data.append(article_object)

    pinecone_store(data)