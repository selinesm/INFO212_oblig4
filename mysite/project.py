from flask import Flask, Blueprint

app = Flask(__name__)
views = Blueprint("views", __name__)

if __name__ == "__main__":
    app.run(debug=True)