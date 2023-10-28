from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Paramètres de connexion à la base de données
db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

def connect_to_database():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except psycopg2.Error as e:
        print("Erreur lors de la connexion à la base de données :")
        print(e)
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lecture_code_barre', methods=['GET', 'POST'])
def lecture_code_barre():
    if request.method == 'GET':
        return render_template('lecture_code_barre.html')
    if request.method == 'POST':
        code_barre = request.form.get('code_barre')
        conn = connect_to_database()
        if conn is None:
            return "Erreur de connexion à la base de données."
        cur = conn.cursor()
        cur.execute("SELECT * FROM bouteilles_de_gaz WHERE code_barres = %s", (code_barre,))
        bouteille = cur.fetchone()
        cur.close()
        if bouteille:
            return render_template('details_bouteille.html', bouteille=bouteille)
        else:
            return "Bouteille non trouvée."

@app.route('/table_bouteille')
def table_bouteille():
    conn = connect_to_database()
    if conn is None:
        return "Erreur de connexion à la base de données."
    cur = conn.cursor()
    cur.execute("SELECT * FROM bouteilles_de_gaz")
    bouteilles = cur.fetchall()
    cur.close()
    return render_template('table_bouteille.html', bouteilles=bouteilles)

@app.route('/edit/<int:bouteille_id>', methods=['GET', 'POST'])
def edit_bouteille(bouteille_id):
    conn = connect_to_database()
    if conn is None:
        return "Erreur de connexion à la base de données."

    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM bouteilles_de_gaz WHERE id = %s", (bouteille_id,))
        bouteille = cursor.fetchone()
        cursor.close()
        conn.close()

        if bouteille:
            return render_template('edit.html', bouteille=bouteille)
        else:
            return "Bouteille non trouvée."

    if request.method == 'POST':
        code_barres = request.form['code_barres']
        numero_machine = request.form['numero_machine']
        description = request.form['description']
        quantite = request.form['quantite']
        emplacement = request.form['emplacement']

        cursor.execute(
            "UPDATE bouteilles_de_gaz SET code_barres = %s, numero_machine = %s, description = %s, quantite = %s, emplacement = %s WHERE id = %s",
            (code_barres, numero_machine, description, quantite, emplacement, bouteille_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return "Bouteille mise à jour avec succès."

@app.route('/add', methods=['GET', 'POST'])
def add_bouteille():
    if request.method == 'GET':
        return render_template('add.html')

    if request.method == 'POST':
        code_barres = request.form['code_barres']
        numero_machine = request.form['numero_machine']
        description = request.form['description']
        quantite = request.form['quantite']
        emplacement = request.form['emplacement']

        conn = connect_to_database()
        if conn is None:
            return "Erreur de connexion à la base de données."

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO bouteilles_de_gaz (code_barres, numero_machine, description, quantite, emplacement) VALUES (%s, %s, %s, %s, %s)",
            (code_barres, numero_machine, description, quantite, emplacement)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return "Bouteille ajoutée avec succès."

if __name__ == '__main__':
    app.run(debug=True)
