import json
import os

from embeddings import get_embedding_model
from vector_store import create_vector_store

CHUNKS_FILE = "data/processed/all_chunks.json"

with open(CHUNKS_FILE, "r", encoding="utf-8") as file:
    chunks = json.load(file)

documents = []

for chunk in chunks:
    documents.append(chunk["content"])

print(f"Loaded {len(documents)} chunks")

embedding_model = get_embedding_model()

print("Generating embeddings...")

vector_db = create_vector_store(
    documents,
    embedding_model
)

os.makedirs(
    "vector_db/faiss_index",
    exist_ok=True
)

vector_db.save_local(
    "vector_db/faiss_index"
)

print("FAISS index created successfully!")