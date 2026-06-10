from langchain_community.vectorstores import FAISS

def create_vector_store(documents, embedding_model):

    vector_db = FAISS.from_texts(
        texts=documents,
        embedding=embedding_model
    )

    return vector_db