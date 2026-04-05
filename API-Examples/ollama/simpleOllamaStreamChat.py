from ollama import chat
from ollama import ChatResponse

# This will block
chatStream = chat(model="gemma4:e2b", messages=[
    {'role': 'system', 'content': 'You should perform basic text generation without reasoning'},
    {'role': 'user', 'content': 'Write a small and nice greeting formula'}
], stream=True)


for chunk in chatStream:
    print(chunk.message.content, end='', flush=True)
