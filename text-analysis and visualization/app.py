from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('topfifty.json') as rf:
        f_context = json.load(rf)
    return render_template('word_cloud_with_d3js.html', value=f_context)


if __name__ == "__main__":
    app.run()
