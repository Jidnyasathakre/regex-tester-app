from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    matches = []
    error = ""

    if request.method == "POST":
        text = request.form.get("text")
        pattern = request.form.get("pattern")

        try:
            matches = re.findall(pattern, text)
        except:
            error = "Invalid regex pattern. Please try again."

    return render_template("index.html", matches=matches, error=error)


if __name__ == "__main__":
    app.run(port=5001, debug=False)
