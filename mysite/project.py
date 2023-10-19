from flask import Flask, Blueprint, render_template
from my_services import app

application = Flask(__name__)
application.register_blueprint(app, url_prefix="/")


if __name__ == "__main__":
    application.run(debug=True)