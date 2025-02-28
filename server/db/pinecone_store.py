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
    data = [
        {"id": "store_sample_vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"id": "store_sample_vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
        {"id": "store_sample_vec3", "text": "Many people enjoy eating apples as a healthy snack."},
        {"id": "store_sample_vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"id": "store_sample_vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
        {"id": "store_sample_vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
    ]
    pinecone_store(data)