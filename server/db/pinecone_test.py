from pinecone_store import pinecone_store
from pinecone_query import pinecone_query

action = "query"

data = [
        {"id": "store_sample_vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"id": "store_sample_vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
        {"id": "store_sample_vec3", "text": "Many people enjoy eating apples as a healthy snack."},
        {"id": "store_sample_vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"id": "store_sample_vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
        {"id": "store_sample_vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
    ]
query = "Tell me about the tech company known as Apple."

if action == "store":
    try:
        pinecone_store(data)
        print("data stored!")
    except:
        print("error while storing")
elif action == "query":
    try:
        results = pinecone_query(query)
        print(results)
    except:
        print("error while querying")
else:
    print("wrong action")

# for testing index existence
# index = pc.Index(index_name)
# print(index.describe_index_stats())