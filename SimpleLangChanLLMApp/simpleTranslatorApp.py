import getpass
import os
from langchain.chat_models import init_chat_model

from langchain_core.messages import HumanMessage, SystemMessage

def print_token_usage(model_output):
    try:
        used_tokens = model_output.response_metadata['token_usage']['total_tokens']
        print(f"Model used {used_tokens} to complete the request")
    except Exception as e:
        print("Error retrieving used tokens")
        print(e)

if not os.environ.get('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = getpass.getpass('Please enter OPEN-AI Api Key')


# Define Text to Text Model
model = init_chat_model("gpt-4o-mini", model_provider="openai")


# Define Messages with types 
messages = [
    SystemMessage("You are a translator and you translate every input from english to italian")
    , HumanMessage("Hello, how are you?")
]

# Direct use of model
output = model.invoke(messages)

print(output.content)
print_token_usage(output)
