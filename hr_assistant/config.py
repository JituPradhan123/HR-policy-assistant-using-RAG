""" All settings for the app live here, in one place."""

from dotenv import load_dotenv
import os

load_dotenv()

## ENV VAR / SECRET

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JIRA_API_KEY = os.getenv("JINA_API_KEY")

## DEFINE PATH - DATA / VECTOR STORE

##  Vectore Store

## 1. In memory like a= 10
## 2. persistent memory - vectors store in folder
## 3. cloude memory
## 2 & 3 use for store vector to file

DATA_FILE_PATH = os.path.join("data","hr_policy.txt")

VECTOR_STORE_PATH = os.path.join("vector_data","faiss_index")

## Models

# llm model

LLM_MODEL_NAME = "openai/gpt-oss-20b"
LLM_MODEL_TEMPERATURE = 0

# Embedding model

EMBEDDING_MODEL_NAME = "jina-embeddings-v5-omni-small"

## Chunk / Text Splitting Config

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrival Results

TOP_K_RESULTS = 3

# System Instructions

SYSTEM_PROMPT=(
    "You are a friendly HR assistant. Always use the search_hr_policy tool to look up"
    "fatch before answering. If the answer isn't in the search results, say you don't know"
    "instead of guessing."
)

def check_api_keys() -> None:
    """ Stop early with a clear message if a required API key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it to your codebase")
    if not JIRA_API_KEY:
        raise ValueError("Missing JIRA_API_KEY. Please add it to your codebase")
        