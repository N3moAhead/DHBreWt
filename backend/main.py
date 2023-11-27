from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/docs')
def docs():
    return render_template("docs.html")

if __name__ == "__main__":
    app.run(debug=True)
