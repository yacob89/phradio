from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', name="Yacob")

@app.route("/programs")
def programs():
    return render_template('programs.html')

if __name__ == "__main__":
    app.debug = True
    app.run()