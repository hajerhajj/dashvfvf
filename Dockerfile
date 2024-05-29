# Utilisez l'image officielle de Python comme base
FROM python:3.10

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposez le port utilisé par Django
EXPOSE 8093

# Commande pour lancer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8093"]
