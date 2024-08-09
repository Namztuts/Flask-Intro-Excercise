# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


#PART ONE
@app.route('/')
def landing():
    html = '''
    <html>
        <body>
            <h1>Calculator</h1>
            <a href="/add">Addition</p>
            <a href="/sub">Subtraction</p>
            <a href="/mult">Multiplication</p>
            <a href="/div">Division</p>
        </body>
    </html>
    '''
    return html

#Addition
@app.route('/add')
def add_page():
    return '''
    <h1>Adding</h1>
        <form method='POST'>
            <input type='number' placeholder='Enter number' name='a'/> +
            <input type='number' placeholder='Enter number' name='b'/>
            <button>Submit</button>
        </form>
        '''
@app.route('/add',methods=['POST'])
def add_result():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = add(a,b)
    return f'''
        <h1>You added numbers!</h1>
        <h3>{a} + {b} = <i>{result}</i></h3>
'''

#Subtraction
@app.route('/sub')
def sub_page():
    return '''
    <h1>Subtracting</h1>
        <form method='POST'>
            <input type='number' placeholder='Enter number' name='a'/> -
            <input type='number' placeholder='Enter number' name='b'/>
            <button>Submit</button>
        </form>
        '''
@app.route('/sub',methods=['POST'])
def sub_result():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = sub(a,b)
    return f'''
        <h1>You subtracted numbers!</h1>
        <h3>{a} + {b} = <i>{result}</i></h3>
'''

#Multiplication
@app.route('/mult')
def mult_page():
    return '''
    <h1>Multiplication</h1>
        <form method='POST'>
            <input type='number' placeholder='Enter number' name='a'/> x
            <input type='number' placeholder='Enter number' name='b'/>
            <button>Submit</button>
        </form>
        '''
@app.route('/mult',methods=['POST'])
def mult_result():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = mult(a,b)
    return f'''
        <h1>You multiplied numbers!</h1>
        <h3>{a} + {b} = <i>{result}</i></h3>
'''

#Division
@app.route('/div')
def div_page():
    return '''
    <h1>Division</h1>
        <form method='POST'>
            <input type='number' placeholder='Enter number' name='a'/> /
            <input type='number' placeholder='Enter number' name='b'/>
            <button>Submit</button>
        </form>
        '''
@app.route('/div',methods=['POST'])
def div_result():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = div(a,b)
    return f'''
        <h1>You divided numbers!</h1>
        <h3>{a} + {b} = <i>{result}</i></h3>
'''

#PART TWO
CALCS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route("/math/<calc>")
def do_math(calc):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = CALCS[calc](a, b)

    return str(result)