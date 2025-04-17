from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPEN_API_KEY")

def generation_openai(query, context):

    prompt = f"""
    You are an advanced AI assistant. The given context are the latest news.
    Provide a relevant and accurate response to the user query.
    
    Context:
    {context}

    User Query:
    {query}

    Based on the provided context, generate a well-informed and concise response that directly addresses the query.
    """

    client = OpenAI(api_key=openai_api_key)

    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )

    return response.output_text


if __name__ == '__main__':
    context = """
    The tech company Apple is known for its innovative products like the iPhone.
    Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.
    Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.
    """
    query = "Tell me about the tech company known as Apple."
    generation = generation_openai(query=query, context=context)
    print(generation)
