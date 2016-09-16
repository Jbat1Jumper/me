from flask import Flask
from nbconvert import export_html
from os import path

app = Flask(__name__)

@app.route("/")
def index():
    return export_html('Jbat1Jumper\'s Website.ipynb')[0]

@app.route("/<notebook>")
def page(notebook):
    file = 'notebooks/{}.ipynb'.format(notebook.replace('_', ' '))
    if path.isfile(file):
        return export_html(file)[0]
    return fourofour(None)

@app.errorhandler(404)
def fourofour(e):
    return export_html('Four O Four.ipynb')[0], 404

if __name__ == "__main__":
    app.run()

