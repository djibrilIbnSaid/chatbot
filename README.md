# chatbot
Chatbot pour le cours de Traitement Automatique des Langues.

## Installation
Créer un environnement virtuel
```bash
python -m venv venv
```
Activer l'environnement virtuel
```bash
source venv/bin/activate
```
Installer les dépendances
```bash
pip install -r requirements.txt
```

## Usage

```bash
python chatbot.py
```

## Travail fait
- [x] Création du projet
- [x] Création du README
- [x] Création du fichier requirements.txt
- [x] Création du fichier traitement.ipynb (pour le traitement des données telecharger sur kaggle pour generer le fichier res.json qui contient les données traitées)
- [x] Création du fichier chatbot.py (Supprimer les mots inutiles, lemmatisation, tokenisation, vectorisation, calcul de la similarité cosinus, affichage des réponses les plus pertinentes en fonction de la question posée par l'utilisateur et aussi pour lancer le chatbot)
