# Generated by Django 2.2.7 on 2020-01-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payement', '0003_auto_20200114_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payement',
            name='status',
            field=models.CharField(choices=[('NP', 'Non Payé'), ('VR', 'Virement Effectué'), ('RE', 'Reçu')], max_length=20),
        ),
    ]