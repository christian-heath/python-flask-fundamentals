from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] = session['counter']+1
    print(session['counter'])
    return render_template("index.html")

@app.route('/add', methods=['post'])
def increment():
    session['counter'] = session['counter']+1
    return redirect('/')

@app.route('/destroy_session', methods=['post'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)