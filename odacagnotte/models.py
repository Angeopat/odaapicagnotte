from django.db import models

# Create your models here.

class Motif(models.Model):
    label = models.CharField(max_length=255)
    montant = models.IntegerField()
    def str_(self):
        return self.label

class Academicien(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=6, primary_key=True)
    photo = models.FileField(upload_to='photo_oda')
    statut = models.BooleanField()

    def str_(self):
        return self.nom

class Paiements(models.Model):
    id_academicien = models.ForeignKey(Academicien, models.SET_NULL, null=True)
    id_motif = models.ForeignKey(Motif, models.SET_NULL, null=True)
    date_paiement = models.DateField(auto_now=True)
    heure_paiement = models.TimeField(auto_now=True)
    unique_key = (date_paiement,id_motif,id_academicien)

    def str_(self):
        return self.date_paiement
