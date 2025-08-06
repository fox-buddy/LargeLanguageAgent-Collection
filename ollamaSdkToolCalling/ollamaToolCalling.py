import ollama
from ollama import ChatResponse
from ollama import chat

# Defining functions
# the functions must be defined on the client side --> User of sdk or ollama API Caller

def add_two_numbers(a: float, b: float) -> float:
    # Model needs this description to choose tool
    """
    Add two numbers

    Args:
        a (set): The first number as a float or int
        b (set): The second number as a float or int

    Returns:
        float: The sum of the two numbers
    """

    return a + b + 1

def substract_two_numbers(a: float, b: float) -> float:
    # Model needs this description to choose tool
    """
    Multiply two numbers

    Args:
        a (set): The first number as a float or int
        b (set): The second number as a float or int that gets substracted from the first one

    Returns:
        float: The difference of the two numbers. a minus b
    """

    return a - b


# To execute after tool usage of LLM Model  --> we need to avoid str is not a function errors
# mappint function names to function calls
tool_map = {
    'substract_two_numbers': substract_two_numbers
    , 'add_two_numbers': add_two_numbers
}


input_messages = [
    {'role': 'user', 'content': 'what is three plus four?'}
]


# we will use the chat endpoint --> possible to insert some history or a system prompt to define behaviour
# Generate Endpoint would just respond without the possibility of data insertion
# When working with the api we can use stream mode in python requests library:
# r = requests.get(url, headers=headers, stream=True, verify=TLS_PATH)

# for raw_response in r.iter_lines():
#     json_response = json.loads(raw_response)
#     .
#     .
#     .

# responses = ollama.chat(
#     model='llama3.1',
#     messages=input_messages,
#     tools=[add_two_numbers, substract_two_numbers],
#     stream=True
# )

# We use a tooling model lika llama to chose the tool
responses: ChatResponse = chat(
    model='llama3.1',
    messages=input_messages,
    tools=[add_two_numbers, substract_two_numbers],
    stream=True
)

# forming tool response texts from chosen tool functions
# the chosen functions are not executed. We need to execute them
input_enhanced_with_tool_results = ''

for chunk in responses:
    # Print model content
    #print(chunk.message.content, end='', flush=True)
    # Print the tool call
    if chunk.message.tool_calls:
        print(chunk.message.tool_calls)
        for tool_call in chunk.message.tool_calls:
            func_name = tool_call.function.name
            args = tool_call.function.arguments
            
            print("\n\n")
            print(f"\nTool call chosen: {func_name}({args})")
            print("\n\n")

            function_result = tool_map[func_name](**args)

            input_message = input_messages[0]['content']
            iteration_tool_result = f"A tool result of input {input_message} tool named <{func_name}> is <{function_result}>, "

            input_enhanced_with_tool_results += iteration_tool_result


#print(input_enhanced_with_tool_results)

input_messages.append(
    {'role': 'system', 'content': f'The answer to the users question is: {function_result}, so use this'}
)


print("\n\n")
print(input_messages)
print("\n\n")

# We use deepseek to output (and see the thinking process)
finalResponses = ollama.chat(
    model='deepseek-r1',
    messages=input_messages,
    stream=True
)

for response in finalResponses:
    # In stream mode every word is a response
    print(response.message.content, end='')

##print(finalResponse.response)