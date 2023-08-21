from app import app
from flask import request
from gpt import start_chat
@app.route("/", methods=['GET'])
def hello():
    return "Hello, World!", 200

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.json['prompt']
    try:
        answer = start_chat(prompt)
    except Exception as e:
        print(e)
        return e.message, 429
    return answer, 200

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
