from langchain_community.vectorstores import FAISS
from knowledge_base.embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector_db = FAISS.load_local(
    "vector_db/faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

def retrieve_documents(query, k=3):

    docs = vector_db.similarity_search(
        query,
        k=k
    )

    return docs