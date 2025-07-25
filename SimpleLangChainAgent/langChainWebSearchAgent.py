import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch

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

search = TavilySearch(max_results=3)
search_results = search.invoke("What is the weather in Stuttgart, Germany?")

print(search_results)

# tool Array for llm model
tools = [search]