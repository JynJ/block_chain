# Étape 1 : Utiliser une image de base Python
FROM python:3.10-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier tous les fichiers du projet dans le conteneur
COPY . .

# Étape 4 : Installer les dépendances Python (si requirements.txt est présent)
# Décommente ces lignes si tu as un fichier requirements.txt
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Définir le script principal à exécuter
CMD ["python", "main.py"]
