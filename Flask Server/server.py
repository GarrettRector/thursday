from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    print(request.data)
    return Response('We recieved something…')


if __name__ == '__main__':
    app.run()
