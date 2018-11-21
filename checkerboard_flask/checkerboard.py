from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight():
    return render_template("checkerboard.html", row = 8, col = 8)

@app.route('/<x>/<y>')
def multi(x, y):
    return render_template("checkerboard.html", row = int(x), col = int(y))

if __name__=="__main__":
    app.run(debug=True)