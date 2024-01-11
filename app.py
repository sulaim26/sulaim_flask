from flask import Flask, render_template, request, jsonify
from openai import OpenAI
app = Flask(__name__,static_url_path='/static')

class ChatAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def generate_completion(self):
        return self.client.chat.completions.create(model="gpt-3.5-turbo", messages=self.messages).choices[0].message.content

assistant = ChatAssistant()

@app.route('/')
def index():
    return render_template('index13.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    assistant.add_message("user", user_input)
    assistant_response = assistant.generate_completion()
    assistant.add_message("assistant", assistant_response)
    return render_template('index13.html', user_input=user_input, assistant_response=assistant_response)

if __name__ == '__main__':
    app.run(host="localhost", port=int("5003"), debug=True)

