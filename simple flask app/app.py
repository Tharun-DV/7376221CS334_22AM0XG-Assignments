from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Student Detail"


@app.route("/getdetail")
def get_detail():
    return "7376221CS334 - THARUN D V"


if __name__ == "__main__":
    app.run(debug=True)
