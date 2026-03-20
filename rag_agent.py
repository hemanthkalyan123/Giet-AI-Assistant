from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = PineconeVectorStore(
    index_name="giet-campus",
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY")
)

retriever = vectorstore.as_retriever(search_kwargs={"k":5})

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

def ask_giet_ai(question):

    docs = retriever.invoke(question)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are an AI assistant for GIET college.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content