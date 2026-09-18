""" Step 3: turn text into vectors using Jina """

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """Return a Jina embedings model and read jina api from env"""
    emb_model = JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
    return emb_model