from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

     # Variáveis globais para armazenar os cliques
cliques = [0, 0, 0, 0, 0]

@app.route('/')
def index():
    return render_template('index.html', cliques=cliques)

@app.route('/click/<int:indice>')
def click(indice):
    if 0 <= indice < len(cliques):
        cliques[indice] += 1    
    return redirect(url_for('index'))

@app.route('/undo/<int:indice>')
def undo(indice):
    if 0 <= indice < len(cliques) and cliques[indice] > 0:
        cliques[indice] -= 1
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global cliques
    cliques = [0, 0, 0, 0, 0]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)