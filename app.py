from flask import Flask
from nbconvert import export_html

app = Flask(__name__)

@app.route("/")
def index():
    return export_html('Jbat1Jumper\\\'s\\ Website.ipnb')[0]

@app.route("/<notebook>")
def page(notebook):
    file = 'notebooks/{}.ipynb'.format(notebook.replace('_', ' '))
    return export_html(file)[0]

if __name__ == "__main__":
    app.run()

