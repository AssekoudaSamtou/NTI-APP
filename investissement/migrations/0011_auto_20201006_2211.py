# Generated by Django 3.1.2 on 2020-10-06 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investissement', '0010_auto_20201006_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='taux',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]