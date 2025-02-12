# Generated by Django 5.0.2 on 2025-02-12 20:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
    ]
