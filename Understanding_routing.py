from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return 'Hi ' + name + '!'

@app.route('/repeat/<x>/<phrase>')
def repeat(x, phrase):
    x = int(x)
    return phrase* x
    
if __name__=="__main__":
    app.run(debug=True)