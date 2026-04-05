from flask import Flask, jsonify, request
from ollama import chat
from ollama import ChatResponse

app = Flask(__name__)

@app.get("/health")
def hello_world():
    return jsonify({"status": "ok"})

@app.post("/chat")
def aiChat():
    request_data = request.get_json()

    print(request_data)

    used_model = request_data.get('model', "gemma4:e2b")
    chat_message = request_data.get('message', "")

    if(len(chat_message) == 0):
        return jsonify({"status": "message is empty"}), 400

    message_pipeline = [
        {'role': 'system', 'content': 'You should perform basic text generation without reasoning'},
        {'role': 'user', 'content': chat_message}
    ]

    # This should run in a Thread against a single Instance. APIS are async and multithreaded. Each Call sould not start a model instance because this reserves a huge amount of memory
    # In Case of ollama it is the service on the server which manages which model is loaded. We can set keep_alive=1 so that the memory is not emptied after 5 minutes https://docs.ollama.com/faq#how-do-i-keep-a-model-loaded-in-memory-or-make-it-unload-immediately
    # It would be a good idea to abstract keep_alive to a startup routine which does a very small request
    # Ollama Server has a default queue of 512 requests. And we could enhance the number of parallel requests (multitasking... so not a real parallel procedure)

    # In Case of Transformers 
    # -> we must Start the model as a Thread (a separate Service that loads a model once)
    # -> Implement a queue Because there is no server that handles this for us

    # In both cases it makes sense to send responses via mqtt (publish via mqtt). Waiting for a gen AI Output transforms the business case from request/response to subscribe result --> request generation --> response ACK --> publish generated result
    # As an Alternative for Transformers queue and response via http in queue

    response: ChatResponse = chat(model=used_model, messages=message_pipeline, keep_alive=1)


    return jsonify({"status": "ok", "model": used_model, "prompt": chat_message, "answer": response.message.content}), 200


if __name__ == "__main__":
    app.run(debug=True)
