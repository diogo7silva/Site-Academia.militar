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
    app.run()
