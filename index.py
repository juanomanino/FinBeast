from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__== '__main__':
    app.run(debug=True)