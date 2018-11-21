from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
# bootstrap html file ^^
@app.route('/users', methods=['POST'])
def create():
    print(request.form)
    print('Name', request.form['name'])
    print('Email', request.form['email'])
    return render_template("created.html")
# form html file ^^
if __name__=="__main__":
    app.run(debug=True)