# Generated by Django 5.0.3 on 2024-07-06 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kategori', '0001_initial'),
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tugas',
            name='kategori',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tugas', to='Kategori.kategori'),
            preserve_default=False,
        ),
    ]
