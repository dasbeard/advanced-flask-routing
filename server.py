#
#
from flask import Flask, render_template, redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    displayAll =True
    return render_template('ninjas.html', display = displayAll)

@app.route('/ninjas/<color>')
def ninja(color):
    displayAll = False
    return render_template('ninjas.html', display=displayAll, color = color)

app.run(debug=True)
