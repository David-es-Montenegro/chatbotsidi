import mysql.connector, random
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

config = {
    'user': 'chatbotsidi',
    'password': 'sidisidi',
    'host': 'chatbotsidi.mysql.pythonanywhere-services.com',
    'database': 'chatbotsidi$banco',
    'raise_on_warnings': True
}

app = Flask(__name__)
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
app.secret_key = '15554'

@app.route('/vagas')
def vagas():
    cursor.execute("SELECT * FROM vagas")
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/candidaturas')
def candidaturas():
    cursor.execute("SELECT * FROM candidaturas")
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/pergunta1', methods=['GET', 'POST'])
def pergunta1():
    if request.method == 'POST':
        resposta = request.form['resposta']
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vagas WHERE id = %s", (resposta,))
        resultado = cursor.fetchone()
        if resultado:
            session['idVaga'] = resposta
            return redirect(url_for('pergunta2'))
        else:
            return render_template('pergunta1erro.html')
    return render_template('pergunta1.html')


@app.route('/pergunta2', methods=['GET', 'POST'])
def pergunta2():
    if request.method == 'GET':
        return render_template('pergunta' + str(random.randint(2,4)) + '.html')
    elif request.method == 'POST':
        resposta = request.form['resposta']
        if resposta == "sim":
             return redirect(url_for('pergunta5'))
        else:
            return render_template('pergunta2negativa.html')

@app.route('/pergunta5', methods=['GET', 'POST'])
def pergunta5():
    if request.method == 'POST':
        resposta = request.form['resposta']
        session['nomeUsuario'] = resposta
        return redirect(url_for('pergunta6'))
    return render_template('pergunta5.html')

@app.route('/pergunta6', methods=['GET', 'POST'])
def pergunta6():
    if request.method == 'POST':
        resposta = request.form['resposta']
        session['email'] = resposta
        return redirect(url_for('pergunta7'))
    return render_template('pergunta6.html')

@app.route('/pergunta7', methods=['GET', 'POST'])
def pergunta7():
    if request.method == 'POST':
        resposta = request.form['resposta']
        session['formacao'] = resposta
        return redirect(url_for('pergunta8'))
    return render_template('pergunta7.html')

@app.route('/pergunta8', methods=['GET', 'POST'])
def pergunta8():
    if request.method == 'POST':
        resposta = request.form['resposta']
        session['tecnologias'] = resposta
        return redirect(url_for('pergunta9'))
    return render_template('pergunta8.html')

@app.route('/pergunta9', methods=['GET', 'POST'])
def pergunta9():
    if request.method == 'GET':
        return render_template('pergunta9.html')
    elif request.method == 'POST':
        resposta = request.form['resposta']
        if resposta == "sim":
            idVaga = session['idVaga']
            nomeUsuario = session['nomeUsuario']
            email = session['email']
            formacao = session['formacao']
            tecnologias = session['tecnologias']
            sql = "INSERT INTO candidaturas (idVaga, nomeUsuario, email, formacao, tecnologias) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (idVaga, nomeUsuario, email, formacao, tecnologias))
            connection.commit()
            session.clear()
            return render_template('candidatado.html')
        else:
            session.clear()
            return render_template('desistencia.html')


#Código Original

#import mysql.connector, random
#from flask import Flask, render_template, request, session, redirect, url_for, jsonify
#
#config = {
#    'user': 'chatbotsidi',
#    'password': 'sidisidi',
#    'host': 'chatbotsidi.mysql.pythonanywhere-services.com',
#    'database': 'chatbotsidi$banco',
#    'raise_on_warnings': True
#}
#
#app = Flask(__name__)
#connection = mysql.connector.connect(**config)
#cursor = connection.cursor()
#app.secret_key = '15554'
#
#@app.route('/vagas')
#def vagas():
#    cursor.execute("SELECT * FROM vagas")
#    results = cursor.fetchall()
#    return jsonify(results)
#
#@app.route('/candidaturas')
#def candidaturas():
#    cursor.execute("SELECT * FROM candidaturas")
#    results = cursor.fetchall()
#    return jsonify(results)
#
#@app.route('/pergunta1', methods=['GET', 'POST'])
#def pergunta1():
#    if request.method == 'POST':
#        resposta = request.form['resposta']
#        cursor = connection.cursor()
#        cursor.execute("SELECT * FROM vagas WHERE id = %s", (resposta,))
#        resultado = cursor.fetchone()
#        if resultado:
#            session['idVaga'] = resposta
#            return redirect(url_for('pergunta2'))
#        else:
#            return render_template('pergunta1erro.html')
#    return render_template('pergunta1.html')
#
#
#@app.route('/pergunta2', methods=['GET', 'POST'])
#def pergunta2():
#    if request.method == 'GET':
#        return render_template('pergunta' + str(random.randint(2,4)) + '.html')
#    elif request.method == 'POST':
#        resposta = request.form['resposta']
#        if resposta == "sim":
#             return redirect(url_for('pergunta5'))
#        else:
#            return render_template('pergunta2negativa.html')
#
#@app.route('/pergunta5', methods=['GET', 'POST'])
#def pergunta5():
#    if request.method == 'POST':
#        resposta = request.form['resposta']
#        session['nomeUsuario'] = resposta
#        return redirect(url_for('pergunta6'))
#    return render_template('pergunta5.html')
#
#@app.route('/pergunta6', methods=['GET', 'POST'])
#def pergunta6():
#    if request.method == 'POST':
#        resposta = request.form['resposta']
#        session['email'] = resposta
#        return redirect(url_for('pergunta7'))
#    return render_template('pergunta6.html')
#
#@app.route('/pergunta7', methods=['GET', 'POST'])
#def pergunta7():
#    if request.method == 'POST':
#        resposta = request.form['resposta']
#        session['formacao'] = resposta
#        return redirect(url_for('pergunta8'))
#    return render_template('pergunta7.html')
#
#@app.route('/pergunta8', methods=['GET', 'POST'])
#def pergunta8():
#    if request.method == 'POST':
#        resposta = request.form['resposta']
#        session['tecnologias'] = resposta
#        return redirect(url_for('pergunta9'))
#    return render_template('pergunta8.html')
#
#@app.route('/pergunta9', methods=['GET', 'POST'])
#def pergunta9():
#    if request.method == 'GET':
#        return render_template('pergunta9.html')
#    elif request.method == 'POST':
#        resposta = request.form['resposta']
#        if resposta == "sim":
#            idVaga = session['idVaga']
#            nomeUsuario = session['nomeUsuario']
#            email = session['email']
#            formacao = session['formacao']
#            tecnologias = session['tecnologias']
#            sql = "INSERT INTO candidaturas (idVaga, nomeUsuario, email, formacao, tecnologias) VALUES (%s, %s, %s, %s, %s)"
#            cursor.execute(sql, (idVaga, nomeUsuario, email, formacao, tecnologias))
#            connection.commit()
#            session.clear()
#            return render_template('candidatado.html')
#        else:
#            session.clear()
#            return render_template('desistencia.html')