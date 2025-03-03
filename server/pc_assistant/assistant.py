# pip install pinecone
# pip install pinecone-plugin-assistant

from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

from dotenv import load_dotenv
import os
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)

# client function
def get_or_create_assistant(assistant_name: str, instructions: str = None):
    """
    return the pinecone assistant with the given name, while pinecone.
    If pinecone assistant with the given name not existing, create it.

    return type: <class 'pinecone_plugins.assistant.models.assistant_model.AssistantModel'>
    """

    # sample return 
    # {   
    #     'created_at': '2025-03-03T20:58:15.910758498Z',
    #     'host': 'https://prod-1-data.ke.pinecone.io',
    #     'instructions': 'Use American English for spelling and grammar.',
    #     'metadata': {},
    #     'name': 'example-assistantv2',
    #     'status': 'Ready',
    #     'updated_at': '2025-03-03T20:58:17.941461008Z'
    # }

    try: 
        # get at assistant
        assistant = pc.assistant.Assistant(
            assistant_name=assistant_name, 
        )
    except:
        if not instructions: 
            instructions = "Use American English for spelling and grammar."
        # Create an assistant
        assistant = pc.assistant.create_assistant(
            assistant_name=assistant_name, 
            instructions=instructions, # Description or directive for the assistant to apply to all responses.
            region="us", # Region to deploy assistant. Options: "us" (default) or "eu".    
            timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
        )

    return assistant

# client function
def upload_file(assistant, file_path: str, metadata: dict):
    """
    upload file in the given file_path with the given metadata to the given assistant.
    return the response from Pinecone.
    """
    response = assistant.upload_file(
        file_path=file_path,
        metadata=metadata,
        timeout=None
    )
    return response

# client function
def chat_assistant(assistant, content: str):
    """
    make a query with given content to the given assistant.
    return a dictionary containing the assistant response message and the documents referenced
    """

    msg = Message(role="user", content=content)
    resp = assistant.chat(messages=[msg]).todict()
   
    assitant_response = resp["message"]
    citations = resp["citations"]

    return {"assitant_response": assitant_response, "citations": citations}