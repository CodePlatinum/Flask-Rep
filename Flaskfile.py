from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    test = ':)'
    return render_template('index.html', test=test)


if __name__ == '__main__':
    app.run(debug=True)

