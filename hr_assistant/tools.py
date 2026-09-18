""" Step 5: wrap the retriever as a tol the agent can call."""
from langchain.tools import tool

def create_search_tool(retriever):
    """Return a @tol function that search the HR Policy"""
    @tool
    def search_hr_policy(question:str)-> str:
        """ Search the HR Policy """
        matching_chunks = retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)
    return search_hr_policy