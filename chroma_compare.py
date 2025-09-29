import chromadb
from dotenv import load_dotenv
import os
import chromadb.utils.embedding_functions as embedding_functions

load_dotenv()  # Load environment variables from .env file

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="cadsr",
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="text-embedding-3-large"
    ),
    configuration={
        "hnsw": {
            "space": "cosine",
            "ef_construction": 200
        }
    }
)

collection.upsert(
    ids=["2296", "58520"],
    documents=[
        "Post Neoplasm Radiation Therapy Progression",
        "Response Symptomatic Deterioration"
    ]
)

results = collection.query(
    query_texts=["Progressive Disease"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)

