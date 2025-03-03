import sys
sys.path.append('./../pc_assistant')
from assistant import get_or_create_assistant, chat_assistant

def query_assisant(assistant_name: str, query: str):
    """
    return {
        "assitant_response": str, 
        "citations": list[citationObject]
    }

    where citationObject format similar to sample format below

    {
        "position": int,
        "references": [
            {
                "file": {
                    "name": "labor_syllabus.pdf",
                    "id": "dad23ed9-dbd2-4f8f-8b46-af83299b9492",
                    "metadata": {
                        "course": "Labor History",
                        "document_type": "Syllabus"
                    },
                    "created_on": "2025-03-03T17:16:43.583239302Z",
                    "updated_on": "2025-03-03T17:17:05.619503901Z",
                    "status": "Available",
                    "percent_done": 1.0,
                    "signed_url": "https://storage.googleapis.com/knowledge-prod-files/144c7a07-1b99-454a-aa2a-558a8a8fb212%2F518144bf-06ac-41bf-8a58-c46809d22812%2Fdad23ed9-dbd2-4f8f-8b46-af83299b9492.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=ke-prod-1%40pc-knowledge-prod.iam.gserviceaccount.com%2F20250303%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250303T204804Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&response-content-disposition=inline&response-content-type=application%2Fpdf&X-Goog-Signature=0c6b348588862239fd2aac0324c8a97cc7e0ab404b7b1d59d3f4a2f070f7b5e717edb5eb6c95b13bff427947fdaddb704141d2d85f95b6c0c963650de4794b5c224e639676ca6be64307d9f0bbcf11fb0ef298a765eae93bfb9c2bd60d57d8cd264a1e1fbe9761452840a55e60441e4f98312af92b86e586b72d2dd72bebd573725e2bb39257b5eb08dc909a59940925ddbbd712ceebef9e61bedb272dba9a8514e6b211b6be664a2f6b4219f9b988189c6717a96f578b376a3c61cc7c14b740a060cdc33c725cd014361f626d3b15b2dba558061899877975a1c66a0c22a2afdeaca02d0d6160273fc9666938f0ff5be29b19719a8eaf572b72c949b8248de3",
                    "error_message": null,
                    "size": 200295.0
                },
                "pages": [
                    2
                ],
                "highlight": null
            }
        ]
    }
    """
    assistant = get_or_create_assistant(assistant_name)
    query_result = chat_assistant(assistant, content=query)
    return query_result