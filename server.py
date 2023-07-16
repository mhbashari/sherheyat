import json

from flask import Flask, render_template

app = Flask(__name__)
all_data = json.load(open("all_data.json"))
topics = [line.strip("\r\n\t ") for line in open("topics_reviewd", encoding="utf-8")]
poets = [line.strip("\r\n\t ") for line in open("poets", encoding="utf-8")]


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
