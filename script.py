from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/packages')
def packages():
    return render_template("packages.html")

@app.route('/download')
def download():
    return render_template("download.html")

if __name__ == "__main__":
    app.run(debug=True)
