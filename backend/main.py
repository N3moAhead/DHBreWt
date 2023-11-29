from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/docs')
def docs():
    return render_template("docs.html")

@app.errorhandler(404)
def not_found(page):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
