from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome!</h1>"

@app.route('/play')
def boxes():
    return render_template("index.html", number = 3)

@app.route('/play/<num>')
def multi_boxes(num):
    return render_template("index.html", number = int(num))

@app.route('/play/<num>/<col>')
def color_boxes(num, col):
    return render_template("index.html", number = int(num), color = col)

if __name__=="__main__":
    app.run(debug=True)