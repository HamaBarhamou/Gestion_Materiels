from django.db import models

# Create your models here.
class TypeMateriel(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.nom)

class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    fonction = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)

class Gerant(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)

class Magasin(models.Model):
    nom = models.CharField(max_length=30)
    gerant = models.ManyToManyField(Gerant)

class Materiel(models.Model):
    nom = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=50)
    typemateriel = models.ForeignKey(TypeMateriel, on_delete=models.CASCADE)
    magasin =  models.ForeignKey(Magasin, on_delete=models.CASCADE)
    personne =  models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nom)