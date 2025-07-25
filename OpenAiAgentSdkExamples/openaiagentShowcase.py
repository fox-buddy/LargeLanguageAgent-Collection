

from agents import Agent, Runner, GuardrailFunctionOutput, InputGuardrail
from pydantic import BaseModel
import asyncio
from agents.exceptions import InputGuardrailTripwireTriggered

class ValidOutput(BaseModel):
    is_math_poem_stockmarket: bool
    reasoning: str

poem_agent = Agent(name="Schillchen", instructions="You are a helpful poet. Please respont in german", handoff_description="Specialist for writing german poems")
math_agent = Agent(name="Albert", instructions="You provide help with mathematical problems. Explain your reasoning and include Examples", handoff_description="Specialist for solving math problems")
financial_agent = Agent(name="Jordan", instructions="You help with financial questions like the Stock market. Always respond with a Warning before your answers", handoff_description="Specialist for financial problems around the market")



guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework, the stock market or wants a poem.",
    output_type=ValidOutput,
)



async def valid_question_guard(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(ValidOutput)

    # tripwire_triggered --> If triggered the execution will be halted
    return GuardrailFunctionOutput(output_info=final_output, tripwire_triggered=not final_output.is_math_poem_stockmarket)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's question",
    handoffs=[poem_agent, math_agent, financial_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=valid_question_guard),
    ],    
)

async def main():
    questions = [
        "I want to buy some Blue Chip Stocks to save some money. What do you think?", 
        "What is 5 added to 6. This is a mathematical question?",
        "What is water made of?"
    ]

    for question in questions:
        try:
            result = await Runner.run(triage_agent, question)
            print(result.final_output)
            print("\n\n")
        except InputGuardrailTripwireTriggered as e:
            print(f"Guardrail triggered by question: {question}")
            print(f"Reason is: {e}")


if __name__ == "__main__":
    asyncio.run(main())