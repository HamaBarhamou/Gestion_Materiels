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

    def __str__(self):
        return '%s' % (self.nom)

class Materiel(models.Model):
    nom = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=50)
    typemateriel = models.ForeignKey(TypeMateriel, on_delete=models.CASCADE)
    magasin =  models.ForeignKey(Magasin, on_delete=models.CASCADE)
    demandes =  models.ManyToManyField(Personne,through='Demande')

    def __str__(self):
        return '%s %s' % (self.nom, self.caracteristique)

class Demande(models.Model):
    person = models.ForeignKey(Personne, on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    date = models.DateField()
    motif_demande = models.CharField(max_length=64)

    def __str__(self):
        return '%s %s' % (self.date, self.motif_demande)
    