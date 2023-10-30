from flask import Flask, render_template, request, jsonify, redirect, url_for
import psycopg2
import os
app = Flask(__name__)

# Paramètres de connexion à la base de données


DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
db_params = {
    'host': DATABASE_HOST,
    'user': DATABASE_USER,
    'password': DATABASE_PASSWORD,
    'port': DATABASE_PORT
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
    if request.method == 'POST':
        code_barre = request.json.get('code_barre')
        if not code_barre:
            return jsonify({'error': 'Veuillez entrer un code-barres.'}), 400
        
        conn = connect_to_database()
        if conn is None:
            return jsonify({'error': 'Erreur de connexion à la base de données.'}), 500

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bouteilles_de_gaz WHERE code_barres = %s", (code_barre,))
        bouteille = cursor.fetchone()
        cursor.close()
        conn.close()

        if bouteille:
            return jsonify({
                'result': f"Résultat pour le code-barres: {code_barre}",
                'data': {
                    'id': bouteille[0],
                    'code_barres': bouteille[1],
                    'numero_machine': bouteille[2],
                    'description': bouteille[3],
                    'quantite': bouteille[4],
                    'emplacement': bouteille[5],
                    'date_ajout': bouteille[6].strftime('%Y-%m-%d %H:%M:%S')
                }
            })
        else:
            return jsonify({'error': 'Aucune bouteille trouvée avec ce code-barres.'}), 404

    return render_template('lecture_code_barre.html')


@app.route('/table_bouteille')
def table_bouteille():
    conn = connect_to_database()
    if conn is None:
        return "Erreur de connexion à la base de données."

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bouteilles_de_gaz")
    bouteilles = cursor.fetchall()
    cursor.close()
    conn.close()

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
    app.run(host='0.0.0.0', debug=True)

