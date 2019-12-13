from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=225, null=True, unique=True)
    telephone = models.CharField(max_length=20, unique=True)
    sexe = models.CharField(max_length=1)

    def __repr__(self):
        return f"{self.nom}"

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Tradeur(Personne):
    avatar = models.ImageField(upload_to="photos/", null=True, blank=True)




