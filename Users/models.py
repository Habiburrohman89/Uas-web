from django.db import models

class Pengguna(models.Model):
    email = models.EmailField(unique=True)
    nama_lengkap = models.CharField(max_length=255)
    tanggal_lahir = models.DateField(null=True, blank=True)
    aktif = models.BooleanField(default=True)
    staf = models.BooleanField(default=False)

    def __str__(self):
        return self.email
