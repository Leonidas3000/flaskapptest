from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello world!, Welcome to group 2 test page"
if __name__ == "__main__":
    app.run()
