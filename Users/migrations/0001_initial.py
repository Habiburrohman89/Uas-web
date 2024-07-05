# Generated by Django 5.0.3 on 2024-07-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('aktif', models.BooleanField(default=True)),
                ('staf', models.BooleanField(default=False)),
            ],
        ),
    ]
