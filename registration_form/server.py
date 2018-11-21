from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secret'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')


@app.route('/')
def home():
    return render_template("survey.html")


@app.route('/result', methods=['post'])
def process():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    if len(session['first_name']) < 1:
        flash("First Name cannot be blank!")
        return redirect('/')
    if session['first_name'].isalpha() is False:
        flash("Name must contain alphabetical characters only.")
        return redirect('/')
    if len(session['last_name']) < 1:
        flash("Last Name cannot be blank!")
        return redirect('/')
    if session['last_name'].isalpha() is False:
        flash("Name must contain alphabetical characters only.")
        return redirect('/')
    if len(session['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if len(session['password']) < 8:
        flash("Password must contain 8 or more characters!")
        return redirect('/')
    if not PASSWORD_REGEX.match(session['password']):
        flash("Password must contain at least one Uppercase letter and number.")
        return redirect('/')
    if session['password'] != session['confirm_password']:
        flash("Passwords do not match!")
        return redirect('/')
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('result.html', first_name=session['first_name'], last_name=session['last_name'], email=session['email'], password=session['password'], confirm_password=session['confirm_password'])

@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We have directed the user to /.")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
