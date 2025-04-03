from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Get environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE")
PINECONE_EMBEDDING_MODEL = os.getenv("PINECONE_EMBEDDING_MODEL")

# client function
def pinecone_query(query):
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    namespace = PINECONE_NAMESPACE
    embedding = get_query_embedding(pc, query)
    results = get_search_results(index, namespace, embedding)
    return results

# helper function 
def get_query_embedding(pc, query):
    embedding = pc.inference.embed(
        model="multilingual-e5-large",
        inputs=[query],
        parameters={
            "input_type": "query"
        }
    )
    return embedding

# helper function 
def get_search_results(index, namespace, embedding):
    results = index.query(
        namespace=namespace,
        vector=embedding[0].values,
        top_k=3,
        include_values=False,
        include_metadata=True
    )
    return results

# sample usage
if __name__ == '__main__':
    query = "Tell me about the tech company known as Apple."
    results = pinecone_query(query)
    print(results)
    for match in results["matches"]:
        print(match["metadata"]["text"])
    