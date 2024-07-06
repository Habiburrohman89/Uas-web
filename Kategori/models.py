from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100, unique=True)
    deskripsi = models.TextField(blank=True)

    def __str__(self):
        return self.nama
