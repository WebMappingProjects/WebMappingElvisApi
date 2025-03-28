# WebMappingElvisApi

## Description du Projet

API django avec django rest framework qui utilise **postgresql** comme sgbd et qui supporte les requetes geospatiales

## Prérequis

- Python 3.9+
- Django 4.2+
- pip

## Installation

### 1. Cloner le Répertoire

```bash
git clone https://github.com/WebMappingProjects/WebMappingElvisApi.git
cd WebMappingElvisApi
```

### 2. Créer un Environnement Virtuel

```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/macOS
# ou 
venv\Scripts\activate  # Sur Windows
```

### 3. Installer les Dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration de la Base de Données

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un Utilisateur Administrateur

```bash
python manage.py createsuperuser
```

## Lancement du Serveur de Développement

```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : `http://127.0.0.1:8000/`

## Structure du Projet

```
WebMappingElvisApi/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── app2/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── WebMappingElvisApi/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── templates/
├── static/
├── media/
├── requirements.txt
└── manage.py
```

## Variables d'Environnement

Créez un fichier `.env` à la racine du projet avec les variables suivantes :

```
SECRET_KEY=votre_clé_secrète
DEBUG=True
DATABASE_URL=votre_url_de_base_de_données
```

## Tests

Pour exécuter les tests :

```bash
python manage.py test
```

## Déploiement

Instructions spécifiques pour le déploiement (Heroku, AWS, etc.)

## Contribution

1. Forker le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Licence

Spécifiez la licence (MIT, Apache, etc.)

## Contact

- Mac Dallas
- roylexstephane@gmail.com
- Lien du Projet : https://github.com/WebMappingProjects/WebMappingElvisApi