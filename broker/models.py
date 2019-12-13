from django.db import models


class Broker(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    site_web = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return f"{self.libelle}"

    def __str__(self):
        return f"{self.libelle}"
