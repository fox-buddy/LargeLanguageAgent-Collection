from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def hello_world():
    return jsonify({"status": "ok"})

@app.post("/chat")
def aiChat():
    date = request.get_json()
    pass


if __name__ == "__main__":
    app.run(debug=True)
