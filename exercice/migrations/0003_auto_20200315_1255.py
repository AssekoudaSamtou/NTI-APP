# Generated by Django 2.2.7 on 2020-03-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercice', '0002_auto_20200307_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='comptes',
            field=models.ManyToManyField(through='exercice.ExerciceCompte', to='compte.Compte'),
        ),
    ]