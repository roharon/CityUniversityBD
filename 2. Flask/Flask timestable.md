# Make times table with web



`./app.py`

```python
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


@app.route('/number', methods='POST')
def times_table():
    value = request.form['value']
    return render_template('times_table.html', val = int(value))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```



`./templates/times_table.html`

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ val }} times table</title>
</head>
<body>

<h1>
    {{ val }} TABLE
</h1>
{% for i in range(1,10) %}

    <p>
    {{ val }} X {{ i }} = {{ val * i }}
    </p>

{% endfor %}

</body>
</html>
```



## Result Screen

When user send `'4`'

![result](https://user-images.githubusercontent.com/4939738/42421565-6042048e-82f9-11e8-8a26-3632fcdb62dd.PNG)

