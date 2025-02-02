from django.db import models

class Project(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nama
