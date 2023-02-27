FROM python:3.9-slim-buster

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY templates/requirements.txt .

# Installer les dépendances depuis le fichier requirements.txt
RUN pip install -r requirements.txt

# Copier le fichier HTML dans le dossier templates
COPY templates/web.html templates/

# Définir le répertoire de travail pour les fichiers Python
WORKDIR /app/back

# Commande de démarrage
CMD ["python", "web_interface_flask.py"]
