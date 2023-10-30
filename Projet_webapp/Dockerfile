
# Utilisez une image de base Python
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . /app

# Installez les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel votre application s'exécutera
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]