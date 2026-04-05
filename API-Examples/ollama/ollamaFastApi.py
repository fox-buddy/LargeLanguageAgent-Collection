from fastapi import FastAPI, HTTPException
from ollama import ChatResponse, chat
from pydantic import BaseModel, Field


app = FastAPI(title="Ollama FastAPI Example")


class ChatMessage(BaseModel):
    role: str = Field(..., examples=["user"])
    content: str


class ChatRequest(BaseModel):
    model: str = Field(default="gemma4:e2b")
    messages: list[ChatMessage]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat")
def post_chat(request: ChatRequest) -> dict[str, str | list[dict[str, str]]]:

    for message in request.messages:
        print(message)

    return {
        "message": "hello"
    }
    # try:
    #     response: ChatResponse = chat(
    #         model=request.model,
    #         messages=[message.model_dump() for message in request.messages],
    #     )
    # except Exception as exc:
    #     raise HTTPException(status_code=500, detail=str(exc)) from exc

    # return {
    #     "model": request.model,
    #     "message": response.message.model_dump(),
    # }
