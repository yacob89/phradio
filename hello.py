from flask import Flask, render_template
import book_of_bible

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', name="Yacob")


@app.route("/programs")
def programs():
    return render_template('programs.html', new_testaments=book_of_bible.new_testaments, old_testaments=book_of_bible.old_testaments)


if __name__ == "__main__":
    app.debug = True
    app.run()
