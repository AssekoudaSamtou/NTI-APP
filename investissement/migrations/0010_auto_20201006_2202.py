# Generated by Django 3.1.2 on 2020-10-06 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investissement', '0009_auto_20201006_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investissement',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='investissements', to='investissement.pack'),
        ),
    ]