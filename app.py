from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variables to store clicks and actions
cliques = [0, 0, 0, 0, 0]
action_stack = []  # Stack to track actions

@app.route('/')
def index():
    return render_template('index.html', cliques=cliques)

@app.route('/click/<int:indice>')
def click(indice):
    if 0 <= indice < len(cliques):
        cliques[indice] += 1
        action_stack.append(('click', indice))  # Store the action
    return redirect(url_for('index'))

@app.route('/undo')
def undo():
    if action_stack:
        action_type, indice = action_stack.pop()  # Get the last action
        if action_type == 'click' and 0 <= indice < len(cliques) and cliques[indice] > 0:
            cliques[indice] -= 1  # Undo the last click
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global cliques
    cliques = [0, 0, 0, 0, 0]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)