import os
import google.generativeai as genai

from dotenv import load_dotenv
from retrieval.retriever import retrieve_documents



load_dotenv()
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(query):

    docs = retrieve_documents(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are GNITS Campus Assistant.

Answer only using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text