
# Important: Ollama must be running on the same machine
# A working solution would be to define a custom container image with Applikation Code and ollama with Models

from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate

from typing import List
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


model = ChatOllama(
    model="gemma3", temperature=0
)

#############################
#####       Simple      #####
#############################
user_input = input("Enter sentence to translate: ")

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", user_input),
]

output = model.invoke(messages)

print("Model Answer:")
print(output)

#############################
#####      Chaining     #####
#############################
input_lang = input("Enter input language: ")
ouput_lang = input("Enter output language: ")
user_input_in_chain = input("Enter sentence to translate: ")

system_template = "You are a translator and you translate every input from {input_language} to {output_language}"
# the whole input will be a variable in the user template
user_template = "{input_text}"

prompt = ChatPromptTemplate.from_messages([("system", system_template), ("user", user_template)])

chain = prompt | model
chain_response = chain.invoke({
    "input_language": input_lang,
    "output_language": ouput_lang,
    "input_text": user_input_in_chain,
})

print("Chain Output:")
print(chain_response)


#############################
#####    Tool Calling   #####
#############################

# Not all tools have been fine tuned for tool usage. Check Ollama site
# in this example i use llama3.1

# defining two functions as a tool

@tool
def validate_user(user_id: int, addresses: List[str]) -> bool:
    """Validate user using historical addresses.

    Args:
        user_id (int): the user ID.
        addresses (List[str]): Previous addresses as a list of strings.
    """
    return True

@tool
def add_two_numbers(a: float, b: float) -> float:
    # Giving the model hints about which tool it can use for the Human Input
    """Add two numbers. Integer values and floats are possible .

    Args:
        a (float): the user ID.
        b (float): Previous addresses as a list of strings.
    """
    return a + b

tool_trained_model = ChatOllama(model="llama3.1", temperature=0)
from langgraph.prebuilt import create_react_agent
agent_executor = create_react_agent(model=tool_trained_model, tools=[validate_user, add_two_numbers])

print("\n\n")

input_message = HumanMessage("""Could you validate user 123? They previously lived at
#     123 Fake St in Boston MA and 234 Pretend Boulevard in
#     Houston TX.""")

for step in agent_executor.stream({"messages": [input_message]}, stream_mode="values"):
    step["messages"][-1].pretty_print()


print("\n\n")
input_message = HumanMessage("Could you add the numbers 5 and 6.7 but only if you have a tool for this")

for step in agent_executor.stream({"messages": [input_message]}, stream_mode="values"):
    step["messages"][-1].pretty_print()


