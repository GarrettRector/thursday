from flask import Flask, Response, request
from ai import ask, append_chat_log

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    question = request.data.decode("UTF-8")
    with open("chatlog.txt", "r") as file:
        chat_log = file.read()
    print(chat_log)
    answer = ask(question, chat_log)
    print(answer)
    append_chat_log(question, answer, chat_log)
    return Response(answer)


if __name__ == '__main__':
    app.run()
