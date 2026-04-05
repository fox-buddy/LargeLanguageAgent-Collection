from ollama import chat
from ollama import ChatResponse

# This will block
response: ChatResponse = chat(model="gemma4:e2b", messages=[
    {'role': 'system', 'content': 'You should perform basic text generation without reasoning'},
    {'role': 'user', 'content': 'Write a small and nice greeting formula'}
])

print(response.message.content)

