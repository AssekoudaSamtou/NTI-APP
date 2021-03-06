# Generated by Django 2.2.7 on 2020-01-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compte', '0001_initial'),
        ('broker', '0001_initial'),
        ('exercice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mois',
            name='compte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mois', to='exercice.ExerciceCompte'),
        ),
        migrations.AddField(
            model_name='compte',
            name='broker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comptes', to='broker.Broker'),
        ),
    ]
