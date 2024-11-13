from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    # Print to the console and also return as response
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 == 0:
            return 'undefined'  # Prevent division by zero
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(debug=True)
