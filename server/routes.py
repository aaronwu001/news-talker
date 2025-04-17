from flask import Flask, jsonify, request
import sys
import os
sys.path.append(os.path.abspath('./generation'))
from generation import generation_openai
sys.path.append(os.path.abspath('./db'))
from pinecone_query import pinecone_query

app = Flask(__name__)

@app.route('/news-feed', methods=['GET'])
def news_feed():
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
    
    return jsonify(news_data)


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({'error': 'Query is required'}), 400

    try:
        pc_results = pinecone_query(query)
        context = ('\n').join([match["metadata"]["text"] for match in pc_results["matches"]])   
        generation = generation_openai(query=query, context=context)
        return jsonify({'generation': generation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
