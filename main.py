from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    ano_atual = datetime.now().year
    nascimento = int(request.form['ano'])
    idade = ano_atual-nascimento

    return render_template('index.html', idade=idade)
if __name__ =='__main__':
    app.run(debug=True)