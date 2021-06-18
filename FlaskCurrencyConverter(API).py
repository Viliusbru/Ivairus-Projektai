from flask import Flask, render_template, request
import requests
from names import names, convert

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    valiuta1 = 'EUR'
    valiuta2 = 'USD'
    skaicius = '20'
    if request.method == 'POST':
        valiuta1 = request.form['from']
        valiuta2 = request.form['to']
        skaicius = request.form['skaicius']

    return render_template('index.html', names=names(), valiuta1=valiuta1, valiuta2=valiuta2, atsakymas=convert(skaicius,valiuta1,valiuta2))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

