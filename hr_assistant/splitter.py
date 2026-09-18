from langchain_text_splitters import RecursiveCharacterTextSplitter

from hr_assistant import config

def split_to_chunks(documents):
    """ Split the document into small small overlapping chunks"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = config.CHUNK_SIZE,
        chunk_overlap = config.CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)
