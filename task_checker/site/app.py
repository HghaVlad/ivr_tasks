import configparser
from flask import Flask, request, render_template
from ..task_1 import get_result
app = Flask(__name__)


config = configparser.ConfigParser()
config.read("config.ini")


@app.route("/")
def home_page():
    return "Welcome"


@app.route("/task_checker", methods=["GET", "POST"])
def task_checker():
    if request.method == "GET":
        task_id = request.args.get("task_number")
        if task_id is None:
            return "Please select a task"
        elif task_id.isdigit() is False:
            return "Please enter the digit"
        elif 0 < int(task_id) <= 1:
            return "Here your link"
    else:
        task_id = request.form.get('task_number')
        site_url = request.form.get("link")
        if task_id is None:
            return "Please select a task"
        elif task_id.isdigit() is False:
            return "Please enter the digit"
        elif site_url is None:
            return "Please enter a link"
        elif int(task_id) == 1:
            tests = get_result(site_url)
            if False in tests:
                return "Fail page"
            else:

                return config['FLAGS']['Task1']


app.run()
