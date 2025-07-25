from langgraph.checkpoint.memory import MemorySaver

import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from langgraph.prebuilt import create_react_agent



if not os.environ.get('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = getpass.getpass("Open AI Api Key eingeben: ")

model = init_chat_model("gpt-4o-mini", model_provider="openai")
memory = MemorySaver()

agent_executor = create_react_agent(model=model, checkpointer=memory, tools=[])

# Provide an ID for every Session 
config = {"configurable": {"thread_id": "hsk748"}}

while True:
    prompt_message = input("Enter Input. Enter quit to continue with new topic: ")

    if(prompt_message == 'quit'):
        break
    
    input_message = HumanMessage(prompt_message)
    for step in agent_executor.stream({"messages": [input_message]}, config, stream_mode="values"):
        step["messages"][-1].pretty_print()



# Begin new Session when providing a new id
config = {"configurable": {"thread_id": "lsu321"}}

while True:
    prompt_message = input("new Session. Enter quit to continue with new topic: ")

    if(prompt_message == 'quit'):
        break

    input_message = HumanMessage(prompt_message)
    for step in agent_executor.stream({"messages": [input_message]}, config, stream_mode="values"):
        step["messages"][-1].pretty_print()


print("Session has ended")