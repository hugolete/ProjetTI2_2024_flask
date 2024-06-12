from flask import render_template,url_for,request
from . import app,models

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/accueil')
def accueil():
    classes = models.classes_lien.query.all()
    return render_template('accueil.html', title='Bienvenue dans notre boutique', liste = type(classes), liste_cat = classes)

@app.route('/menu')
def menu():
    return render_template('menu.html',title='Menu')

@app.route('/tous_produits')
def tous_produits():
    liste_vehicules = models.Vue_vehicule_categorie.query.all()
    return render_template('tous_produits.html', title='Nos produits', liste_prod=liste_vehicules)

@app.route('/produits_categorie')
def produits_categorie():
    classe = request.args.get('classe')
    liste_vehicules = models.Vue_vehicule_categorie.query.filter_by(classe=classe)
    return render_template('produits_categorie.html',title='Nos produits',produits = liste_vehicules,typeprod = type(liste_vehicules))