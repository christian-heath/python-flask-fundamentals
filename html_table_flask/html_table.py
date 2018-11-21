from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def table():
    student_info = (
       {'first_name' : 'Michael', 'num' : '1', 'last_name' : 'Choi', 'age' : 35},
       {'first_name' : 'John', 'num' : '2', 'last_name' : 'Supsupin', 'age' : 30 },
       {'first_name' : 'Mark', 'num' : '3', 'last_name' : 'Guillen', 'age' : 25},
       {'first_name' : 'KB', 'num' : '4', 'last_name' : 'Tonel', 'age' : 27}
    )
    return render_template("index.html", students = student_info)

if __name__ =="__main__":
    app.run(debug=True)