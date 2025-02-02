# Generated by Django 5.0.3 on 2024-07-05 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tugas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('tanggal_dibuat', models.DateTimeField(auto_now_add=True)),
                ('batas_waktu', models.DateField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tugas_ditugaskan', to='Users.pengguna')),
                ('pembuat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tugas_dibuat', to='Users.pengguna')),
            ],
        ),
    ]
