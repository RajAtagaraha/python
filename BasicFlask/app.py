from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/hello/<user>')
def hello_user(user):
    return "Hello %s!" % user


if __name__ == "__main__":
    app.run()
