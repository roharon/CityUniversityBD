from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <form action='number' method=post>
    <p><input type=number name=value>
    <p><input type=submit value=Send>
    </form>
    """


@app.route('/number', methods=['POST','GET'])
def times_table():
    value = request.form['value']
    return render_template('times_table.html', val = int(value))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
