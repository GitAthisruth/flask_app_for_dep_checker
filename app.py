from flask import Flask
import finding_python_ast

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World,from Flask!"


print(finding_python_ast())