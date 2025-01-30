from flask import Flask

app = Flask(__name__)

def add(x, y):
    return x + y

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
