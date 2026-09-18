""" Step 4: store the embeding in faiss so that we can search them later."""

import os
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embedding import get_embeddings_model

# Build vector store

def build_vector_store(chunks):
    """Embed every chunk and build a searchable FAISS index in memory."""
    embedding_model = get_embeddings_model()
    return FAISS.from_documents(chunks,embedding_model)

# Save vector store

def save_vector_store(vector_store,path:str=config.VECTOR_STORE_PATH)-> None:
    """Save the faiss index to disk so that we no ned to build every time."""
    vector_store.save_local(path)

# Load vector store

def load_vector_store(path:str=config.VECTOR_STORE_PATH):
    """Load previously saved fais index vector store"""
    embedding_model = get_embeddings_model()
    return FAISS.load_local(path,embedding_model,allow_dangerous_deserialization=True)

def vector_store_exists(path:str=config.VECTOR_STORE_PATH)-> bool:
    """Check if a saved FAISS index already exists on disk"""
    return os.path.exists(os.path.join(path,"index.faiss"))

def get_retriever(vector_store, k:int = config.TOP_K_RESULTS):
    """ retrive and return the top_k matching chunks"""
    return vector_store.as_retriever(search_kwargs={"k":k})