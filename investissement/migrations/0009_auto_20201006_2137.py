# Generated by Django 3.1.2 on 2020-10-06 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investissement', '0008_investissement_taux'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=14)),
                ('duree', models.PositiveSmallIntegerField()),
                ('taux', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='investissement',
            name='duree',
        ),
        migrations.RemoveField(
            model_name='investissement',
            name='taux',
        ),
        migrations.AlterField(
            model_name='investissement',
            name='pack',
            field=models.ForeignKey(choices=[('1', 'Profit Mensuel'), ('2', 'Bloqué')], on_delete=django.db.models.deletion.DO_NOTHING, related_name='investissements', to='investissement.pack'),
        ),
    ]