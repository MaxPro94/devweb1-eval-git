from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = 'villes.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def index():
    cursor = get_db().cursor()
    cursor.execute('SELECT ville_nom FROM villes_france_free')
    villes = cursor.fetchall()
    return render_template('index.html', villes=villes)

if __name__ == '__main__':
    app.run(debug=True)