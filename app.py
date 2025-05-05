from flask import Flask, render_template, request
from zxcvbn import zxcvbn

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    password = ""
    feedback = None

    if request.method == "POST":
        password = request.form["password"]
        result = zxcvbn(password)
        strength = result["score"]
        feedback = result["feedback"]
    return render_template("index.html", strength=strength, password=password, feedback=feedback)

if __name__=="__main__":
    app.run(debug=True)