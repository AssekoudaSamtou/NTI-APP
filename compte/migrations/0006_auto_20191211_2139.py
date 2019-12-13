# Generated by Django 2.2.7 on 2019-12-11 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0005_compte_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='tradeur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comptes', to='tradeur.Tradeur'),
        ),
    ]
