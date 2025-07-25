import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_core.messages import SystemMessage, HumanMessage

from langgraph.prebuilt import create_react_agent

##########################################
#####       Helper functions         #####
##########################################
def print_token_usage(model_output):
    try:
        used_tokens = model_output.response_metadata['token_usage']['total_tokens']
        print(f"Model used {used_tokens} Tokens to complete the request")
    except Exception as e:
        print("Error retrieving used tokens")
        print(e)

##########################################

# Define Text to Text Model
if not os.environ.get('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = getpass.getpass('Please enter OPEN-AI Api Key')


model = init_chat_model("gpt-4o-mini", model_provider="openai")

# define web search Tool
if not os.environ.get('TAVILY_API_KEY'):
    os.environ['TAVILY_API_KEY'] = getpass.getpass('Please enter Tavily API Key')





user_question = input("What is your weather question? ")
weather_question = user_question if len(user_question) > 0 else "What is the weather in Stuttgart, Germany?"
messages = [
    SystemMessage("""
                  You are a weather expert. 
                  You have access to a web search tool. 
                  You use this tool if you get asked for the weather and respond accordingly. 
                  If you get other questions, then respond with an excuse""")
    , HumanMessage(weather_question)
]

search = TavilySearch(max_results=3)
search_results = search.invoke(weather_question)
# Test search
# print(search_results)

# define llm model with tools
tools = [search]

#model_with_tools = model.bind_tools(tools)
# send chat to model --> Will not content a response
# response = model_with_tools.invoke(messages)
# print(f"Message content: {response.text()}\n")
# print(f"Tool calls: {response.tool_calls}")
# print_token_usage(response)


# Create Agent
agent_executor = create_react_agent(model, tools)

response = agent_executor.invoke({"messages": messages})

for message in response["messages"]:
    message.pretty_print()