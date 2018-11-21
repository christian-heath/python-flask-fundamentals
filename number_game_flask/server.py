from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'ThisisSecret'
import random

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0,101) 
    print(session['number'])
    return render_template("index.html", playagain='none')

@app.route('/guess', methods=['post'])
def submit():
    guess=request.form['guess']
    if guess.isdigit() == False:
        return render_template("index.html", status= 'danger', hotorcold = 'Integers only, please!', playagain = 'none')
    if int(guess)==session['number']:
        return render_template("index.html", status = 'success', hotorcold = 'Congratulations!', playagain = 'visible')
    if int(guess)>session['number']:
        return render_template("index.html", status = 'danger', hotorcold = "Too high! Try again!", playagain = 'none')
    if int(guess)<session['number']:
        return render_template("index.html", status = 'danger', hotorcold = "Too low! Try again!", playagain = 'none')
    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)