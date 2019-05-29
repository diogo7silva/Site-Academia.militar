from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    from datetime import datetime
    horas = datetime.today().hour
    minutos = datetime.today().minute
    segundos = datetime.today().second
    frase1 = ("São {} horas, {} minutos e {} segundos!".format(horas, minutos, segundos))
    if horas < 4:
        frase2 = ('Boa Noite !')
    elif horas < 12:
        frase2 = ('Bom dia !')
    elif horas < 20:
        frase2 = ('Boa Tarde !')
    else:
        frase2 = ('Boa Noite !')
    return render_template('index.html', t1=frase1, t2=frase2)

@app.route('/mensagem')
def mensagem():
    return render_template('mensagem.html')

@app.route('/missão')
def missão():
    return render_template('missão.html')

@app.route('/visão')
def visão():
    return render_template('visão.html')

@app.route('/valores')
def valores():
    return render_template('valores.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registo')
def registo():
    return render_template('registo.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')


if __name__ == '__main__':
    app.run(debug=True)
