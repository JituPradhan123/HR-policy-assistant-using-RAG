""" Connect the llm to the brain of the brain of the assistant """

from langchain_groq import ChatGroq
from hr_assistant import config

def get_llm():
    """ Return groq chat model. reads groq api from env"""
    llm = ChatGroq(
        model = config.LLM_MODEL_NAME,
        temperature=config.LLM_MODEL_TEMPERATURE
    )
    return llm