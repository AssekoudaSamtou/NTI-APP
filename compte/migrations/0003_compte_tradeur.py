# Generated by Django 2.2.7 on 2020-01-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tradeur', '0001_initial'),
        ('compte', '0002_auto_20200106_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte',
            name='tradeur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comptes', to='tradeur.Tradeur'),
        ),
    ]
