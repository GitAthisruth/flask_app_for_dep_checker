from flask import Flask
from utils.dependency_check import  dependency_check



app = Flask(__name__)

file_to_check = input("Give a valid file_name (.py): ").strip()
folder_path = "C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab"

@app.route("/")
def home():
    return dependency_check(file_to_check,folder_path)


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)