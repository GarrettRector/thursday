import secrets
from flask import Flask, Response, request, session
from ai import ask, append_interaction_to_chat_log

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key


@app.route('/', methods=['POST'])
def get_data():
    question = request.data
    question = str(question)
    print(question)
    chat_log = session.get('chat_log')
    answer = ask(question, chat_log)
    print(answer)
    session['chat_log'] = append_interaction_to_chat_log(question, answer, chat_log)
    return Response(answer)


if __name__ == '__main__':
    app.run()
