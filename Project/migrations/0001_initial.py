# Generated by Django 5.0.3 on 2024-07-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
