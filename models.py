from . import app,db
from flask_sqlalchemy import SQLAlchemy

class Vue_vehicule_categorie(db.Model):
    id_véhicule = db.Column(db.Integer, primary_key=True)
    modele = db.Column(db.String(50), nullable=True)
    classe = db.Column(db.String(50), nullable=True)
    id_type_vehicule = db.Column(db.Integer, nullable=False)
    type_vehicule = db.Column(db.String(50), nullable=True)
    prix = db.Column(db.Integer, nullable=True)
    lien = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'{self.id_vehicule} : {self.modele} : {self.classe} : {self.id_type_vehicule} : {self.poids} : {self.vmax} : {self.nb_chevaux} : {self.conso_carburant} : {self.prix}'

class classes_lien(db.Model):
    id_classelien = db.Column(db.Integer, primary_key=True)
    classe = db.Column(db.String(50), nullable=True)
    lien = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'{self.classe} : {self.lien}'