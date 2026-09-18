""" step 7: build the agent that ties llm and search tool togeather. """

from langchain.agents import create_agent

from hr_assistant import config

def create_hr_agent(llm,tools):
    """ Return a LangChain agent that can call our tools and answer the questions """
    chat_agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT
    )
    return chat_agent