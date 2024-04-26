from flask import Flask, render_template

runner = Flask(__name__)

@runner.route('/index/')
def index():
	fruits = ['apple', 'orange', 'pineapple', 'banana']
	coureses = ('C', 'C++', 'JAVA', 'PYTHON', 'REACTJS')
	emp_details = {'name' : 'idiot', 'age' : 20, 'address' : 'pavai'}
	return render_template('index.html', fruit = fruits, coures = coureses, emp = emp_details)

if __name__ == '__main__':
	runner.run(debug = True)