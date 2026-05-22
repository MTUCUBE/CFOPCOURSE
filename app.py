from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/notation")
def notation():
    return render_template("notation.html")

@app.route("/f2l")
def f2l():
    return render_template("f2l.html")

@app.route("/oll")
def oll():
    return render_template("oll.html")

@app.route("/pll")
def pll():
    return render_template("pll.html")

if __name__ == "__main__":
    app.run(debug=True)