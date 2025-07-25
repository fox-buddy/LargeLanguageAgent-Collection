import getpass
import os
from langchain.chat_models import init_chat_model

from langchain_core.prompts import ChatPromptTemplate

def print_token_usage(model_output):
    try:
        used_tokens = model_output.response_metadata['token_usage']['total_tokens']
        print(f"Model used {used_tokens} Tokens to complete the request")
    except Exception as e:
        print("Error retrieving used tokens")
        print(e)

if not os.environ.get('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = getpass.getpass('Please enter OPEN-AI Api Key')


# Define Text to Text Model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# a variable named language is defined in the system_template
system_template = "You are a translator and you translate every input from english to {language}"
# the whole input will be a variable in the user template
user_template = "{text}"

model_prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)

# Define prompt --> Fill template with variables in a dictionary
model_prompt = model_prompt_template.invoke({"language": "Spanish", "text": "Hello, how are you?"})

# show model prompt. Consists of messages list
#print(model_prompt)

# Use prompt in model
output = model.invoke(model_prompt)
print(output.content)
print_token_usage(output)
