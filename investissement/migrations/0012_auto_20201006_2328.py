# Generated by Django 3.1.2 on 2020-10-06 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investissement', '0011_auto_20201006_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='investissement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investissement',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investissement',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]