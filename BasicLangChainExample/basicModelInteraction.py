import getpass
import os
from langchain.chat_models import init_chat_model

if not os.environ.get('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = getpass.getpass('Please enter OPEN-AI Api Key')


model = init_chat_model("gpt-4o-mini", model_provider="openai")

output = model.invoke("Hello GPT. Please tell ma a small Haiku")

print("Model Answer:")
print(output.content)

