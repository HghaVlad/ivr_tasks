import configparser
from flask import Flask, request, render_template
from ivr_tasks.task_checker.task_1 import get_result
app = Flask(__name__)


config = configparser.ConfigParser()
config.read("config.ini")


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/task_checker", methods=["GET", "POST"])
def task_checker():
    if request.method == "GET":
        return render_template("form_page.html")
    else:
        task_id = request.form.get('task_number')
        site_url = request.form.get("link")
        if task_id is None:
            return render_template("fail_form.html", error="Пожалуйста выберите номер задания")
        elif site_url is None:
            return render_template("fail_form.html", error="Пожалуйста введите ссылку")
        elif "http://" not in site_url:
            return render_template("fail_form.html", error="Пожалуйста введите ссылку")
        elif int(task_id) == 1:
            if site_url[-1] != "/":
                site_url = site_url + "/"
            tests = get_result(site_url)
            names = ["Тест 1", "Тест 2", "Тест 3"]
            if False not in tests:
                return render_template("unsuccess_page.html", res_tests=zip(names, tests))
            else:
                return render_template("success_page.html", flag=config['FLAGS']['Task1'] )


app.run()
