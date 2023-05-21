from flask import Flask, render_template, request, redirect
from data import data

import datetime
import os

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/admin')
def admin():
    return render_template('admin.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)