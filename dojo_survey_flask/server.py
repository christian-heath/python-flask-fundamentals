from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def home():
    return render_template("survey.html")


@app.route('/result', methods=['post'])
def process():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    if len(session['name']) < 1:
        flash(u"Name is required.", 'errorname')
        return redirect('/')
    if len(session['comment']) < 1:
        flash("Comment is required.")
        return redirect('/')
    if len(session['comment']) > 255:
        flash("Comment must be less than 255 characters.")
        return redirect('/')
    return render_template('info.html', name = session['name'], dojo_location = session['dojo_location'], favorite_language = session['favorite_language'], comment = session['comment'])

if __name__ == "__main__":
    app.run(debug=True)
