from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'secret'
import random
import datetime


def activitylog(location, gold, time):
        message = "<p>You leave the "+str(location)+" with "+str(gold)+" gold at "+str(time)+'</p>'
        session['activity'] += message

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = "Hello! Welcome to Ninja Gold!"
    return render_template("index.html", gold=session['gold'], activity=session['activity'])


@app.route('/process_money', methods=['post'])
def submit():
    buildingName = request.form['building']
    time = datetime.datetime.now()
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        session['gold'] += gold
        activitylog(buildingName, gold, time)
    if request.form['building'] == 'cave':
        gold = random.randrange(5,11)
        session['gold'] += gold
        activitylog(buildingName, gold, time)
    if request.form['building'] == 'house':
        gold = random.randrange(2,6)
        session['gold'] += gold
        activitylog(buildingName, gold, time)
    if request.form['building'] == 'casino':
        gold = random.randrange(-50,51)
        session['gold'] += gold
        activitylog(buildingName, gold, time)
    return redirect('/')


@app.route('/reset', methods=['get'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
