from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index2():
    return render_template('index2.html')
