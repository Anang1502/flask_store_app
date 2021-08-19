from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/hello/<user>')
def hello(user):
    return render_template()


if __name__ == '__main__':
    app.run(debug=True)
