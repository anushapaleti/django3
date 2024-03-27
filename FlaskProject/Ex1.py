from flask import *

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'

@app.route('/h')
def hello1():
    return 'Hey u what do u want'

@app.route('/e/<int:emp1>')
def show_emp(emp1):
    return 'EMP ID is %d' %emp1

@app.route('/e1/<float:emp1>')
def show_emp1(emp1):
    return 'EMP ID is %f' %emp1

@app.route('/e2/<string:emp1>')
def show_emp2(emp1):
    return 'EMP ID is %s' %emp1

@app.route('/a')
def index():
    return render_template("Hello.html")

if __name__ == "__main__":
    app.run(debug=True)