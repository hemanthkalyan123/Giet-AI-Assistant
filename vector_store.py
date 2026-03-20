import os
import json
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone, ServerlessSpec

# Load API keys
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "giet-campus"

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

print("Pinecone index ready")

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = []

# Load context text
with open("giet_context.txt", "r", encoding="utf-8") as f:
    context = f.read()
    documents.append(Document(page_content=context))

# Load JSON data
with open("giet_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    text = f"""
Branch: {item['branch']}
Fee: {item['fee']}
Description: {item['description']}
"""
    documents.append(Document(page_content=text))

print("Loaded documents:", len(documents))

# Upload to Pinecone
vectorstore = PineconeVectorStore.from_documents(
    documents=documents,
    embedding=embeddings,
    index_name=index_name
)

print("Upload complete!")

