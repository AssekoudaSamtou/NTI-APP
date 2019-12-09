from django.db import models


class Broker(models.Model):
    libelle = models.CharField(max_length=50)
    site_web = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.libelle}"
